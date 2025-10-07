![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-00A98F?style=for-the-badge&logo=python&logoColor=white)
![CAD](https://img.shields.io/badge/AutoCAD-000000?style=for-the-badge&logo=autodesk&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

# Project Aegis — 실무 자동화 포트폴리오

> 20년 현장 경험과 AI 협업으로 만든 금속 구조물 제작 자동화 시스템
> 견적·발주·공정관리 전 과정을 데이터 기반으로 재구성했습니다.

---

## ⚙️ 시스템 구성 (2025.10)

### 📊 견적 자동화 시스템 (v0.85)

* **BOM 기반 자동 견적서 생성**
* 1,482개 자재 DB, Excel 템플릿 기반 출력
* **기술:** Python, Pandas, Openpyxl, Streamlit

### 🏗️ 공정 관리 시스템 (v0.5)

* 프로젝트 중심 진행 관리
* 납기·서류·매출 통계 시각화
* **기술:** SQLite, Streamlit → Supabase 예정

---

## 🚀 주요 성과

| 지표        | 개선 전       | 개선 후 |
| --------- | ---------- | ---- |
| 견적서 작성 시간 | 2 시간       | 10 분 |
| 계산 오류율    | 15%        | 0%   |
| 실제 운영     | 두호 실증 3 개월 |      |

---

## 🧩 기술 하이라이트

* **고급 모델 검색:** difflib + pandas 유사도 매칭
* **템플릿 자동경로 해결:** `resolve_template_path()`
* **엑셀 캐시 최적화:** `st.cache_data` 활용
* **모듈화 구조:** launcher ↔ quotation ↔ WIP 3-tier

---

## 📝 기술 블로그 & 데모

* 블로그: [drummer78.tistory.com](https://drummer78.tistory.com)
* 데모 영상: [YouTube Link](https://youtu.be/rVLi1zquamE)
* 변경 이력: [`docs/changelog_public.md`](docs/changelog_public.md)

---

## 🧱 공개 범위 정책

이 레포는 **비식별 샘플 데이터** 를 사용합니다.
실제 업체명, 고객명, 연락처 등은 모두 가명으로 처리되었습니다.

---

## 📦 프로젝트 구조 (공개 버전)

```
Project-Aegis/
├─ app/
│   ├─ quotation_app_sample_v0.85.py
│   ├─ wip_app_sample_v0.5.py
│   └─ launcher_sample.py
├─ database/
│   └─ samples/
│        ├─ material_database_sample.xlsx
│        └─ wip_database_sample.db
├─ docs/
│   ├─ showcase/
│   │   ├─ case_study_01.md
│   │   ├─ case_study_02.md
│   │   └─ ...
│   ├─ architecture.md
│   └─ changelog_public.md
├─ README.md
└─ LICENSE
```

---

## 🔄 운영 전략 요약

| 항목           | 원칙                                           |
| ------------ | -------------------------------------------- |
| **레포 목적**    | 실무 자동화 성과물 포트폴리오 / 비식별화된 데모 공개               |
| **공개주기**     | 월 1회 (주요 기능 완성 후 블로그 링크 추가)                  |
| **코드 공개범위**  | 로직은 100%, 실제 데이터·고객명은 0%                     |
| **문서연결**     | README → 기술블로그 / YouTube 데모 링크               |
| **업데이트 트리거** | 내부 changelog 갱신 → `.public-include` 동기화 → 커밋 |

---

## 🧠 추가 아이디어

* README 상단 배지 추가 (기술스택 시각화)
* docs/showcase 폴더에 케이스 스터디 시리즈 추가
* 커밋마다 블로그 링크 자동 추가
* 공개 버전 태그(`v0.85-public`, `v0.9-supabase`) 전략 적용

---

**📜 License:** MIT
**📧 Contact:** 배성준 (Aegis_BIMer) — drummer78.tistory.com
