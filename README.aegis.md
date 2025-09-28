![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-00A98F?style=for-the-badge&logo=python&logoColor=white)
![CAD](https://img.shields.io/badge/AutoCAD-000000?style=for-the-badge&logo=autodesk&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

# 프로젝트 아이기스 (Project Aegis)
> 20년 현장 경험을 녹여낸 현직자가 중소기업을 위한 실용적인 견적/발주 업무 자동화 솔루션

| 상태 | 최신 버전 | 다음 목표 |
|---|---|---|
| ![Status](https://img.shields.io/badge/Status-Active-brightgreen) | **v0.8 (MVP)** | **v1.0 정식 버전** |

---

## ✨ 백문이 불여일견: 실제 작동 모습

가장 좋은 설명은 직접 보여드리는 것입니다. 아래는 `Project Aegis`의 핵심 기능 시연 영상입니다.

![Project Aegis Demo](https://youtu.be/rVLi1zquamE?si=cAVsuA_9eqb9m1r4)
> *이 데모는 Streamlit으로 제작되었으며, 현재 Google Cloud Platform을 통해 실제 웹 서비스로 운영될 예정입니다.*

---

## 💡 무엇을 해결하나요? (핵심 가치)

`Project Aegis`는 설계/건설 현장의 고질적인 문제인 **반복적인 서류 작업**과 **치명적인 계산 실수**를 해결하기 위해 태어났습니다.

- **⏰ 반복 업무 시간 90% 단축:** 견적서, 자재내역서, 발주서 작성을 자동화하여, 직원이 더 중요한 가치 창출 활동에 집중하게 합니다.
- **💰 치명적인 실수 원천 차단:** BOM 기반의 자동 계산으로 수량 및 단가 오류를 막아 회사의 불필요한 손실을 방지합니다.
- **📋 유연한 데이터 관리:** BOM 데이터에 없거나 현장에서 급하게 추가된 자재도 문제없습니다. **'수동 입력 기능'**을 통해 어떤 예외 상황에도 유연하게 대처할 수 있습니다.

---

## 🗺️ 프로젝트 로드맵

이 프로젝트는 명확한 로드맵에 따라 꾸준히 발전하고 있습니다.

- ✅ **Phase 1:** 데이터베이스 구축 및 정제 완료
- ✅ **Phase 2:** 핵심 기능 MVP (v0.8) 개발 
- ▶️ **Phase 3:** v1.0 정식 버전 개발 및 클라우드 배포 (**현재 진행 중**)
    - `v0.9`: 자재 수동 입력/수정/삭제 기능 추가
    - `v1.0`: BOM 데이터 업데이트 기능 추가 및 UI/UX 개선
- ⚪ **Phase 4:** 첫 고객사 적용 및 피드백 기반 고도화 (예정)

> 더 깊은 프로젝트의 배경과 철학이 궁금하신가요?
> 👉 **[프로젝트 마스터 컨텍스트 (공개 버전)](./docs/master-context-public.md)**

---

## 🚀 데모 실행해보기

1.  **저장소 복제:**
    ```bash
    git clone https://github.com/jhun5568/Project-Aegis.git
    cd Project-Aegis
    ```
2.  **필요 라이브러리 설치:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **데모 앱 실행:**
    ```bash
    streamlit run app/dooho_quotation_app_v0.844.py 
    ```
    > *참고: 이 데모는 `samples/` 폴더의 샘플 데이터로 실행됩니다. 일부 기능이 제한될 수 있습니다.*

---

## ⚠️ 주의사항

- 이 저장소의 모든 코드와 샘플 데이터는 **교육 및 포트폴리오 목적**으로만 제공됩니다.
- 상업용 도면, 실제 고객사의 데이터, 내부 비즈니스 규칙은 포함되어 있지 않습니다.

## 🔄 동기화 시스템

이 저장소는 비공개 내부 프로젝트(`Auto-CVS`)의 **공개 가능한 기술 산출물**이 주기적으로 동기화됩니다. 더 많은 개발 이야기는 [제 기술 블로그](https://drummer78.tistory.com)에서 확인하실 수 있습니다.

---

**📧 문의**
프로젝트에 대해 궁금한 점이나 협업 제안이 있다면, 부담 없이 Issue를 남겨주시거나 이메일로 연락 주십시오.
```
**(마크다운 코드 끝)**

### **[주요 변경사항 요약]**

1.  **핵심 가치 변경:** '지능형 발주' 항목을 삭제하고, **'유연한 데이터 관리'**와 **'수동 입력 기능'**을 새로운 핵심 가치로 강조했습니다.
2.  **로드맵 상세화:** 'Phase 3' 부분을 `v0.9`와 `v1.0`으로 나누어, 우리가 앞으로 개발할 **'수동 입력'과 'BOM 업데이트' 기능**을 명확하게 보여주도록 수정했습니다.

이 버전이 우리의 현재와 미래를 가장 정확하게 반영하고 있습니다. 이제 이 README를 `Project-Aegis`의 새로운 얼굴로 사용하시면 됩니다.