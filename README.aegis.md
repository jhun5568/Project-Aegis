![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CAD](https://img.shields.io/badge/AutoCAD-000000?style=for-the-badge&logo=autodesk&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

# 프로젝트 아이기스 (Project Aegis)

> **20년 경력의 설계 종사자가 Python을 활용해 설계 및 발주 업무의 반복적인 업무를 자동화하는 오픈소스 프로젝트입니다.**
>
> 이 저장소는 기술 데모와 학습 결과물을 공유합니다. (내부 비즈니스 전략 및 기밀 자료 제외)

## ✨ 프로젝트 목표

실무에서 마주치는 두 가지 주요 문제를 해결하는 도구를 개발합니다.

1.  **편의점 인테리어 설계 자동화:** CAD 도면에서 자재 수량(BOM)을 자동 추출하고, 견적서와 발주서를 생성합니다.
2.  **금속 구조물 제작 프로세스 자동화:** CAD 도면에서 자재 수량(BOM)을 자동 추출하고, 조달 및 사급 금속구조물 발주 프로세스에서 발생하는 문서 작업을 자동화합니다.

## 🛠️ 주요 기술 스택

*   **주력:** Python, ezdxf (CAD 파싱), pandas (데이터 처리), openpyxl (Excel 자동화)
*   **시각화/배포:** Streamlit (웹 대시보드)
*   **데이터 관리:** SQLite, CSV
*   **협업/관리:** GitHub, GitHub Actions

## 🗂 프로젝트 구조
```
Project-Aegis/
├── src/ # 소스 코드
│ ├── learning/ # Python & ML 학습 기록
│ ├── steel_structure/ # 금속 구조물 제작 프로세스 자동화 (Core)
│ ├── convenience_store/ # 편의점 인테리어 자동화 (Co-Core)
│ ├── expansion/ # Revit/Dynamo 연구 자료
│ └── deepdive_project / #팀 프로젝트 외부 공개용 폴더
├── docs/ # 문서
│ └── showcase/ # 시연 자료 (시나리오, 기술 스택)
├── data/ # 데이터
│ └── samples/ # 샘플 데이터 (CSV, Excel)
├── scripts/ # 스크립트
│ └── tools/ # 유틸리티 스크립트
└── README.md # 이 파일
```

## 🚀 시작하기 (데모 실행)

가장 쉬운 시작점은 편의점 인테리어 자동화입니다.

1.  **의존성 설치:** `pip install -r requirements.txt`
2.  **예제 실행:** `src/convenience_store_automation/dxf_to_bom.py` 스크립트를 실행해보세요.
3.  **샘플 데이터:** `data/samples/` 디렉토리의 샘플 DXF 파일이 어떻게 분석되는지 확인합니다.
4.  **대시보드 체험 (Optional):** `streamlit run src/convenience_store_automation/dashboard.py`로 간단한 대시보드를 실행할 수 있습니다.

## 📊 주요 기능 및 결과물

*   **DXF 파서:** AutoCAD 도면(.dxf)에서 벽체 길이, 집기 수량, 공간 면적 등을 자동 추출.
*   **BOM 생성기:** 추출된 데이터를 기반으로 Bill of Materials를 생성하고 Excel 파일로 출력.
*   **견적서 생성기:** 단가 DB와 연동하여 자동 견적서 초안 작성.
*   **발주서 자동화:** BOM을 기반으로 협력사별 발주서를 자동 생성.

## ⚠️ 주의사항

- 이 저장소의 모든 코드와 샘플 데이터는 **교육 및 포트폴리오 목적**으로만 제공됩니다.
- 상업용 도면, 실무 데이터, 내부 비즈니스 규칙은 포함되어 있지 않습니다.

## 🔄 동기화 시스템

이 저장소는 비공개 개인 프로젝트의 **공개 가능한 기술 산출물**이 주기적으로 동기화됩니다. 더 많은 배경 이야기는 [개발 이야기](https://url-to-your-blog.com)에서 확인하실 수 있습니다.

---

**📧 문의**
궁금한 점이 있으면 Issue를 남겨주세요!