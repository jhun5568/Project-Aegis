![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-00A98F?style=for-the-badge&logo=python&logoColor=white)
![CAD](https://img.shields.io/badge/AutoCAD-000000?style=for-the-badge&logo=autodesk&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

# 프로젝트 아이기스 (Project Aegis)

> **실용적인 엑셀 자동화 솔루션: Python과 Pandas를 활용한 업무 프로세스 최적화**

> 🎉 **새 소식**: v1.0 프로토타입 개발 완료! Streamlit 기반 대시보드로 엑셀 데이터베이스를 시각화하고 관리할 수 있습니다. (v5.2)

> 이 저장소는 기술 데모와 학습 결과물을 공유합니다. (내부 비즈니스 전략 및 기밀 자료 제외)

## ✨ 프로젝트 목표

실무에서 마주치는 반복적인 업무를 자동화하는 도구를 개발합니다.

1.  **엑셀 기반 데이터 관리:** 전문가 지식의 체계적 정리 및 활용
2.  **자동화 보고서 생성:** 자재 명세서 및 발주서 자동 생성 (개발 중)
3.  **재고 통합 관리:** 실시간 재고 추적 및 최적 발주량 계산 (예정)

## 🛠️ 주요 기술 스택

*   **주력:** Python, Pandas (데이터 처리), Openpyxl (Excel 자동화)
*   **데이터 관리:** 엑셀 기반 데이터베이스
*   **시각화/배포:** Streamlit (웹 대시보드)
*   **협업/관리:** GitHub, GitHub Actions

## 🗂 프로젝트 구조
```
Project-Aegis/
├── 📂learning/ # Python & ML 학습 기록
├── 📂docs/ # 문서
│ └── 📂showcase/ # 시연 자료 (시나리오, 기술 스택)
├── 📂 samples/              # 📄 데모 실행에 필요한 '샘플 데이터'
│   └── sample_database.xlsx
│
├── 📜 dashboard.py           # 🚀 메인 Streamlit 대시보드 실행 파일
├── 📜 bom_generator.py       # (예시) BOM 생성 핵심 로직
├── 📜 utils.py               # (예시) 공통 함수 모음
│
├── 📜 README.md              # 쇼룸의 얼굴
├── 📜 requirements.txt        # 필요한 부품 목록
└── 📜 .gitignore             # 버전 관리에서 제외할 파일 목록
└── README.md # 이 파일

```


## 🚀 시작하기 (데모 실행) - 구현 중

가장 쉬운 시작점은 Streamlit 대시보드 데모입니다.

1.  **의존성 설치:** `pip install -r requirements.txt`
2.  **대시보드 실행:** `streamlit run src/steel_structure/dashboard.py`
3.  **기능 체험:** 
    - 엑셀 데이터베이스 현황 조회
    - 모델별 자재 목록 확인
    - 자재 검색 및 필터링
4.  **샘플 영상 데이터:** `/docs/showcase/videos` 디렉토리의 샘플 영상 업로드.

## 📊 주요 기능 및 결과물

*   **✅ 엑셀 데이터베이스 리더:** Pandas 기반 엑셀 데이터 읽기 및 조회
*   **✅ Streamlit 대시보드:** 웹 기반 데이터 시각화 및 관리
*   **🔄 자동 보고서 생성기:** openpyxl을 이용한 자재내역서/발주서 자동 생성 (개발 중)
*   **⚪ 견적서 생성기:** 제품 가격 DB와 연동하여 자동 견적서 초안 작성 
*   **⚪ 자재산출서:** 자재 단가 DB와 연동하여 실제 자재비를 통한 손익 계산 (예정) 

## ⚠️ 주의사항

- 이 저장소의 모든 코드와 샘플 데이터는 **교육 및 포트폴리오 목적**으로만 제공됩니다.
- 상업용 도면, 실무 데이터, 내부 비즈니스 규칙은 포함되어 있지 않습니다.

## 🔄 동기화 시스템

이 저장소는 비공개 개인 프로젝트의 **공개 가능한 기술 산출물**이 주기적으로 동기화됩니다. 더 많은 배경 이야기는 [개발 이야기](https://drummer78.tistory.com)에서 확인하실 수 있습니다.

---

**버전 관리 기록**:
- v4.3 (2025.09.17): 엑셀+Pandas 최적화 전략
- v5.0 (2025.09.18): 프로토타입 완성
- v5.2 (2025.09.19): 시스템 안정성 및 성능 개선

**📧 문의**
궁금한 점이 있으면 Issue를 남겨주세요!