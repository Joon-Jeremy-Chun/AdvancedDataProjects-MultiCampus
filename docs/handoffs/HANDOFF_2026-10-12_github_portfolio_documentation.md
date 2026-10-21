# 인계 — 상세 GitHub 포트폴리오 문서

날짜: 2026-10-12 · 담당: Codex · 대상: AdvancedDataProjects-MultiCampus

## 요청과 완료 상태

[팩트] 사용자는 제안한 정리 방향대로 진행하고 여러 이력서를 참고해 README를
매우 상세하고 보기 좋게 작성하도록 요청했다. 로컬 문서 정리는 완료했다.
원격 GitHub 게시, staging, commit, push는 수행하지 않았다.

## Git 상태와 보존 경계

- 작업 브랜치 `master`, 기준 HEAD `06ddbb4`.
- origin: `https://github.com/Joon-Jeremy-Chun/AdvancedDataProjects-MultiCampus`.
- 기존 추적 자료 80개 중 수정한 파일은 루트 `README.md` 하나다.
- 이번 문서·에셋·지침·기록은 로컬 변경/미추적 상태이며 index는 비어 있다.
- 기존 일반 노트북 54개, 체크포인트 13개, Python 4개, 원본 PNG 6개,
  개발 메모 2개를 그대로 유지했다.
- 기존 로컬 `BP_BG_prediction-Machine_Deep_Learning/DataSets/`의 CSV 5개는
  442,451,117바이트로 남아 있다. 내용·이용 조건은 미확인이고 새 ignore 규칙 대상이다.

후속 세션에서 이 날짜의 상태를 현재 상태로 가정하지 말고 Git을 다시 확인한다.

## 산출물

| 문서·경로 | 내용 |
|---|---|
| [루트 README](../../README.md) | 세 팀 프로젝트·네 컬렉션, 개인 기여, 대표 읽기 경로, 재현 상태 |
| [전기차 README](../../Electric_vehicle_trend-Visualization_Analysis/README.md) | 검색 추이·역할·수집·비교·원본 그림·방법 한계 |
| [건강 README](../../BP_BG_prediction-Machine_Deep_Learning/README.md) | 변수·모델·분류/회귀·보고 성과/저장 지표·그림·평가 경계 |
| [암호화폐 연구 README](../../cryptocurrency_sentiment-Deep_Learning/README.md) | 영어 NLP·감성 지수·가격 모델·추천·시각화·지표 해석 |
| [암호화폐 통합 README](../../crypto_market_prediction_project-DB_DL_combined/README.md) | Coinpan·한국어 LSTM·6개 파일 안내·외부 효과 |
| [PROJECT_EVIDENCE.md](../PROJECT_EVIDENCE.md) | 자료명·페이지·기여·기간 차이·수상·셀별 지표 근거 |
| [REPRODUCIBILITY.md](../REPRODUCIBILITY.md) | 읽기/실행 구분, 입력·의존성·모델·DB·재현 경계 |
| [NOTEBOOK_CATALOG.md](../NOTEBOOK_CATALOG.md) | 노트북 67개와 Python 4개; 셀 수·저장 출력·오류 셀 목록 |
| [assets/readme/](../../assets/readme/) | SVG 표지 5개, 저장 출력 PNG 4개, [출처](../../assets/readme/SOURCES.md) |
| [.gitignore](../../.gitignore) | 환경·캐시·환경 변수 파일·기존 로컬 건강 데이터 제외 |
| [memory/](../../memory/) | 현재 상태·지도·선택 이유·세션 이력 갱신 |

처음 만든 공용·Claude·Codex 지침은 유지했다. 공개 문서는 기존 영어를 유지했다.

## 참고 자료와 핵심 정정

[팩트] 이력서 2026·2024, CV 2023과 프로젝트 소개 PDF 3개를 읽었다.
스캔 형태인 2024 이력서의 프로젝트 페이지는 이미지로 확인했다.
원본 PDF·연락처·개인 파일 경로를 공개 문서나 이미지로 복사하지 않았다.
출처 파일명과 관련 페이지는 근거표에 있다.

- 개인 기여와 팀 전체 성과를 나누었다. 영어 감성 모델의 협업자 기록도 유지했다.
- 건강 프로젝트 기간은 이력서 August–October와 소개 September–October가 달라
  Autumn 2021로 표시하고 두 출처를 설명했다.
- 건강 소개 자료의 79%/91%와 회귀 오차는 보고 수치로 표시했다.
  저장된 92.28% 이진 혈당 분류 및 표준화 MSE와 혼동하지 않는다.
- 영어 LSTM 셀 43–47은 `evaluate()[0]`을 accuracy라고 출력하지만 로그에서 loss다.
  실제 `acc`는 약 0.68–0.70이고 README에 각 값을 함께 적었다.
- 암호화폐 소개 자료의 combined 80%는 회고된 시장 방향 성과다.
  분류 정확도·가격 모델 loss·추천 적합도와는 다른 지표이며 프로토콜은 미확인이다.
- EV smoothing 셀의 반복 lag와 국가 비교 행 제거, health split 전 scaling,
  가격 모델의 날짜 순서·shift·검증 분리 한계를 설명했다. 코드는 변경하지 않았다.
- MongoDB/AWS/웹은 소개 자료의 팀 범위이고 저장소에서는 MySQL 인터페이스가 보인다.
  완성된 frontend나 현재 운영 서비스의 존재를 주장하지 않는다.

## 검증

- 모든 기존 노트북 67개의 JSON은 초기 정적 조사에서 파싱됐다.
  저장 출력 65개·저장 오류 20개는 현재 실행 결과가 아니다.
- 생성·수정 Markdown의 UTF-8, 상대 링크/그림/앵커, 코드 fence와 공백을 확인했다.
  원래 감성 지수 메모의 기존 trailing spaces는 원본 보존 대상으로 제외했다.
- 최종 검사 대상은 생성·수정 Markdown 20개와 상대 링크/그림 참조 342개다.
  깨진 대상·앵커는 없었고 catalog는 기존 노트북 67개와 Python 4개를 모두 포함했다.
- SVG 5개의 XML 파싱, 추출 PNG 4개의 원본 출력 바이트 일치를 확인했다.
- 루트 데스크톱/좁은 화면과 프로젝트 README 4개를 임시 HTML로 렌더링해 확인했다.
  로컬 미리보기는 실제 GitHub 렌더링 확인을 대신하지 않는다.
- `git diff --check`, 추적 변경 경계, 빈 index, 기존 CSV 개수·크기를 확인했다.
- 데이터 본문 조회, 모델 학습, crawler 실행, DB 접속, 설치 호환성 검증은 수행하지 않았다.

## 후속 작업

1. 사용자 검토 후 명시적 게시 요청이 있으면 diff와 대상 파일을 다시 확인하고
   구체적인 파일만 stage한다. 기존 데이터·원본 PDF·임시 미리보기는 포함하지 않는다.
2. 수상 증서·최종 평가 정의·초기 프로젝트 날짜를 추가 자료로 보완할 수 있다.
   현재 README는 해당 출처 수준과 차이를 공개한다.
3. 환경 복원이 요청되면 외부 입력/모델을 확보하고 대표 실험 하나부터 별도 작업본에서
   검증한다. 고정 버전 requirements를 현재 관찰만으로 만들지 않는다.
4. 파일명 변경·체크포인트 정리·자료 이동/삭제는 별도 구체 범위와 보존 방안을 정한다.

정리 관련 최신 상태는 [작업 상태](../../memory/project_task_status.md),
전체 배경은 [세션 기록](../../memory/research_direction_log.md)를 따른다.
