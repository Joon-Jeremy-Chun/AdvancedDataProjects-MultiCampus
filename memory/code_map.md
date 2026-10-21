# 저장소 지도와 최초 현황

기준일: 2026-10-11. 초기 HEAD: `06ddbb4`, 로컬 브랜치: `master`.
아래 기존 자료 개수는 지침 생성 전 `git ls-files` 기준이다.

## 기존 프로젝트 자료

| 경로 | 추적 자료 | 최초 확인 수준 |
|---|---|---|
| [혈압·혈당 예측](../BP_BG_prediction-Machine_Deep_Learning/) | 노트북 12개, PNG 6개 | 프로젝트 README 없음; 모델 성능·대표본·실행 순서 미확인 |
| [전기차 분석](../Electric_vehicle_trend-Visualization_Analysis/) | 노트북 20개 | 프로젝트 README 없음; 수상·결론의 근거와 대표본 미확인 |
| [암호화폐 감성 분석](../cryptocurrency_sentiment-Deep_Learning/) | 노트북 33개, Markdown 2개 | 프로젝트 README 없음; 학습·평가·지수 산출 연결 관계 미확인 |
| [암호화폐 시장 예측](../crypto_market_prediction_project-DB_DL_combined/) | 노트북 2개, Python 4개 | 프로젝트 README 없음; 데이터 수집·예측·웹 연계의 실제 범위 미확인 |
| [루트 README](../README.md) | Markdown 1개 | 영어 소개와 프로젝트 설명 존재; 상세 주장별 근거 대조 필요 |

[팩트] 합계 80개 추적 파일: 노트북 67개, Python 4개, PNG 6개,
Markdown 3개. `.ipynb_checkpoints/` 안의 추적 노트북은 혈압·혈당 3개,
전기차 10개로 총 13개다. 복사본과 대표본의 동일성은 미확인이다.

## 확인한 Python 경로

- [coinpan_crawling.py](../crypto_market_prediction_project-DB_DL_combined/coinpan_crawling.py)
- [coinpan_index_c.py](../crypto_market_prediction_project-DB_DL_combined/coinpan_index_c.py)
- [yahoo_fin_ex.py](<../crypto_market_prediction_project-DB_DL_combined/갈대 AI/yahoo_fin_ex.py>)
- [갈대_AI_LSTM_최적화.py](<../crypto_market_prediction_project-DB_DL_combined/갈대 AI/갈대_AI_LSTM_최적화.py>)

파일 존재와 일부 import를 확인했다. 파일명만으로 역할·실행 순서를 확정하지 않았다.

## 노트북 정적 확인

[팩트] Python 표준 JSON 파서로 추적 노트북 67개를 모두 읽었으며
파싱 오류는 0개였다. 체크포인트도 이 집계에 포함된다.

| 정적 확인 항목 | 노트북 수 | 해석 범위 |
|---|---:|---|
| 저장된 출력이 하나 이상 존재 | 65 | 현재 실행 성공을 뜻하지 않음 |
| `output_type=error` 출력이 하나 이상 존재 | 20 | 과거 저장된 오류; 현재 실패 여부 미확인 |
| 소스에 Windows 드라이브 절대경로 패턴 존재 | 30 | `[A-Za-z]:[\\/]` 정규식 탐지; 실제 경로 사용 여부 추가 확인 필요 |
| 소스에 `/content/` 문자열 존재 | 40 | 문자열 탐지; Colab 의존성과 실행 가능 여부 추가 확인 필요 |

행별 집합은 중복될 수 있다. 셀 실행, 학습, 데이터 조회, 결과 검산은 수행하지 않았다.

## 로컬 데이터와 환경 파일

[팩트] 최초 미추적 경로
`BP_BG_prediction-Machine_Deep_Learning/DataSets/`에 CSV 5개가 있다.
합산 크기는 442,451,117바이트다. 내용, 이용 조건, 민감성은 미확인이다.
이번 준비 작업의 산출물이 아니므로 향후 staging 대상과 구분해야 한다.

[팩트] 최초 루트 `.gitignore`가 없으며 추적 파일 목록에
`requirements.txt`, `pyproject.toml`, `environment.yml`, `Pipfile`은 없다.
현재 확인한 Python은 3.11.5다. 이 버전이 원래 프로젝트와 호환되는지는 미확인이다.

## 2026-10-11에 만든 운영 문서

| 경로 | 역할 |
|---|---|
| [AGENTS.md](../AGENTS.md) | 공용 규칙과 GitHub 문서 품질 기준 |
| [CLAUDE.md](../CLAUDE.md) | Claude 진입 지침 |
| [CODEX.md](../CODEX.md) | Codex 진입 지침과 Windows 작업 참고 |
| [MEMORY.md](MEMORY.md) | 짧은 기록 인덱스 |
| [project_philosophy.md](project_philosophy.md) | 목적과 선택 이유 |
| [project_task_status.md](project_task_status.md) | 미완료 작업과 완료 조건 |
| [research_direction_log.md](research_direction_log.md) | 세션별 확인·결정 이력 |
| [github_cleanup_plan.md](../docs/github_cleanup_plan.md) | 정리 단계와 공개 문서 틀 |
| [docs/handoffs/](../docs/handoffs/) | 에이전트·세션 간 인계 |

구조가 바뀌면 이 지도를 갱신하고, 상세 과거 현황은 세션 기록에 보존한다.

## 2026-10-12 — 현재 문서와 연결 관계

[팩트] 위 표는 정리 전 현황이다. 현재는 [루트 README](../README.md)와
프로젝트 README 4개가 있고, 세 팀 프로젝트를 네 코드 컬렉션으로 설명한다.
암호화폐 연구 폴더와 수집·한국어 NLP 폴더는 같은 최종 프로젝트의 두 자료 묶음이다.

| 현재 진입점 | 대표 내용과 연결 |
|---|---|
| [전기차 README](../Electric_vehicle_trend-Visualization_Analysis/README.md) | 국가별 1년/5년 비교와 장기 검색 추이; 팀원의 담당 범위와 원본 그림 |
| [건강 예측 README](../BP_BG_prediction-Machine_Deep_Learning/README.md) | 종합 혈당·선형·트리·숲 실험; 과제 소개의 혈압/혈당 성과와 저장 실험 지표 구분 |
| [암호화폐 연구 README](../cryptocurrency_sentiment-Deep_Learning/README.md) | 영어 NLP → 감성 지수 → 가격 모델 → 추천 → 시각화; 팀 기여와 지표 해석 |
| [암호화폐 통합 README](../crypto_market_prediction_project-DB_DL_combined/README.md) | Coinpan crawler 2개, 한국어 LSTM 노트북 2개, 실험 Python 파일 2개 |
| [PROJECT_EVIDENCE.md](../docs/PROJECT_EVIDENCE.md) | 이력서·프로젝트 소개의 출처, 기간 차이, 기여·성과·셀 근거 |
| [REPRODUCIBILITY.md](../docs/REPRODUCIBILITY.md) | 외부 데이터·배열·모델·DB·의존성과 실행 경계 |
| [NOTEBOOK_CATALOG.md](../docs/NOTEBOOK_CATALOG.md) | 체크포인트 포함 기존 노트북 67개와 Python 4개; 저장 출력·오류 셀 목록 |
| [assets/readme/](../assets/readme/) | SVG 표지 5개, 원본 출력 PNG 4개, 그림 출처 문서 |

[팩트] 기존 일반 노트북 54개와 체크포인트 13개는 모두 유지했다.
새 `.gitignore`는 로컬 환경·캐시·`.env`와 기존 건강 `DataSets/`를 제외한다.
기존 CSV 5개, 442,451,117바이트는 디스크에 남아 있다. 추적된 체크포인트는
ignore 규칙으로 제거되지 않는다. 의존성 manifest와 검증된 실행 환경은 아직 없다.

대표 노트북의 소스·선택 출력과 Python 흐름을 추가로 읽었지만, 새로운 학습·수집·DB 작업은
실행하지 않았다. 문서와 그림의 확인 범위는 최신 인계와 근거표를 따른다.
