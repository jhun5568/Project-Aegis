name: Sync selected files to Project-Aegis

on:
  workflow_dispatch:
  push:
    branches: [ main ]
    paths:
      - '.public-include'
      - '.public-exclude'
      - 'src/**'
      - 'docs/**'
      - 'data/**'
      - 'families/**'
      - 'scripts/**'
      - 'README.aegis.md'
      - 'LICENSE'

jobs:
  sync:
    runs-on: ubuntu-latest

    env:
      AEGIS_OWNER: ${{ vars.AEGIS_OWNER || 'jhun5568' }}
      AEGIS_REPO: ${{ vars.AEGIS_REPO || 'Project-Aegis' }}
      AEGIS_BRANCH: ${{ vars.AEGIS_BRANCH || 'main' }}

    steps:
      - name: Checkout PRIVATE repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          path: private-repo

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Run Python sync script
        run: |
          cd private-repo
          python - << 'EOF'
          import os
          import shutil
          import glob
          from pathlib import Path

          # 기본 경로 설정
          root = Path('.').resolve()
          export_dir = root / 'public_export'
          
          # 기존 export 디렉토리 정리
          if export_dir.exists():
              shutil.rmtree(export_dir)
          export_dir.mkdir()

          print("=== Processing .public-include ===")
          
          # .public-include 파일 읽기
          include_file = root / '.public-include'
          if not include_file.exists():
              raise FileNotFoundError("❌ .public-include file not found!")
          
          with open(include_file, 'r', encoding='utf-8') as f:
              patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
          
          # 각 패턴 처리
          for pattern in patterns:
              print(f"Processing pattern: {pattern}")
              matches = glob.glob(pattern, recursive=True)
              
              if not matches:
                  print(f"  ⚠️ No files matched: {pattern}")
                  continue
                  
              for match in matches:
                  src_path = Path(match)
                  if src_path.is_file():
                      dest_path = export_dir / src_path
                      dest_path.parent.mkdir(parents=True, exist_ok=True)
                      shutil.copy2(src_path, dest_path)
                      print(f"  ✅ Copied: {src_path}")
                  elif src_path.is_dir():
                      dest_path = export_dir / src_path
                      shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                      print(f"  ✅ Copied directory: {src_path}")

          print(f"=== Export completed: {len(list(export_dir.rglob('*')))} files ===")
          EOF

      - name: Debug export contents
        run: |
          cd private-repo
          echo "=== Export directory structure ==="
          find public_export -type f | head -20
          echo "Total files: $(find public_export -type f | wc -l)"

      - name: Sync to public repo
        run: |
          cd private-repo
          
          git config --global user.name "Auto Sync Bot"
          git config --global user.email "actions@github.com"

          # Public repo 클론
          git clone --depth 1 "https://${{ secrets.AEGIS_TOKEN }}@github.com/${{ env.AEGIS_OWNER }}/${{ env.AEGIS_REPO }}.git" out_repo
          
          cd out_repo
          git checkout -B "${{ env.AEGIS_BRANCH }}"

          # Public repo 내용 완전히 교체
          rm -rf * .[!.]* ..?* 2>/dev/null || true
          cp -r ../public_export/* .
          cp -r ../public_export/.[!.]* . 2>/dev/null || true
          cp -r ../public_export/..?* . 2>/dev/null || true

          git add -A
          if git diff --cached --quiet; then
            echo "No changes to commit."
          else
            TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
            git commit -m "chore(sync): update from Auto-CVS-Project at ${TS}"
            git push origin "${{ env.AEGIS_BRANCH }}"
          fi

      - name: Cleanup
        run: |
          rm -rf private-repo/out_repo private-repo/public_export