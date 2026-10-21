# 2026-10-11 — Codex / 저장소 지침 생성과 작업 준비 인계

## 요청과 범위

[팩트] 사용자는 GitHub 상세 정리를 목적으로 `quant-trading-system`의
Claude·Codex·공용 지침을 참고한 지침 생성과 작업 준비를 요청했다.
생성할 파일 종류와 경로를 대화에서 먼저 공유했다.

## 생성한 파일

- [공용 AGENTS.md](../../AGENTS.md)
- [Claude 진입 지침](../../CLAUDE.md)
- [Codex 작업 지침](../../CODEX.md)
- [기록 인덱스](../../memory/MEMORY.md)
- [목적과 원칙](../../memory/project_philosophy.md)
- [저장소 지도](../../memory/code_map.md)
- [작업 상태](../../memory/project_task_status.md)
- [조사·결정 기록](../../memory/research_direction_log.md)
- [GitHub 정리 계획](../github_cleanup_plan.md)
- 이 인계 문서

## 확인한 근거와 준비 상태

[팩트] 초기 로컬 branch `master`, HEAD `06ddbb4`.
origin은 `https://github.com/Joon-Jeremy-Chun/AdvancedDataProjects-MultiCampus`이다.
기존 추적 파일 80개 중 노트북 67개를 JSON으로 읽었다.
모두 파싱됐고 저장 출력 65개, 오류 출력 20개,
Windows 드라이브 경로 패턴 30개, `/content/` 문자열 40개를 확인했다.

[팩트] 4개 프로젝트 각각의 README와 확인 대상 의존성 manifest는 없다.
기존 루트 README 주장의 상세 근거는 아직 대조하지 않았다.
각 프로젝트의 대표본·성능·개인 기여·수상·실행 가능 여부는 미확인이다.

[팩트] 참고 지침의 핵심 협업 원칙을 가져와 GitHub 설명·자료 보존·재현 수준
표시에 맞췄다. 지침은 영어, 인계와 사용자용 기록은 한국어로 작성했다.
참고한 문서와 설계 이유는 [목적 기록](../../memory/project_philosophy.md)과
[세션 로그](../../memory/research_direction_log.md)에 있다.

## 기존 작업과 변경 경계

[팩트] 최초 미추적 경로는
`BP_BG_prediction-Machine_Deep_Learning/DataSets/`이며 CSV 5개,
총 442,451,117바이트다. 데이터 내용과 공개 권한은 미확인이다.
이 데이터는 기존 사용자 자료이며 이번 생성 파일과 구분해야 한다.

[팩트] 변경 범위는 위 새 Markdown 파일 10개다. 기존 README·노트북·스크립트·
이미지·데이터의 내용 또는 위치를 수정하지 않았다.
노트북 실행·학습·크롤링·데이터 다운로드·commit·push·원격 변경은 수행하지 않았다.

## 다음 작업

[추론] 대표 파일과 실제 흐름을 확인해 프로젝트별 근거 표를 만들고,
그 다음 루트 README와 프로젝트 README를 작성하는 순서가 적절하다.
[정리 계획](../github_cleanup_plan.md)과
[작업 상태](../../memory/project_task_status.md)를 따라 진행한다.
문서 언어, 개인 기여, 수상 근거, 재현 범위는 필요한 시점에 사용자 맥락을 보완한다.

## 문서 검증

[팩트] 생성 문서 10개를 UTF-8로 읽었고, 상대 링크 60개의 대상이 모두 존재했다.
문자 치환 오류, 마지막 줄바꿈 누락, 줄 끝 여분 공백, 코드 블록 구분자 불균형은 없었다.
외부 링크는 이번 작업에서 열어 확인한 OpenAI 공식 지침 문서다.

[팩트] `git status --short`는 기존 `DataSets/`와 새 지침·기록 경로만
미추적으로 표시했다. 기존 추적 파일 diff는 없고 HEAD는 `06ddbb4`로 유지됐다.
`git diff --check`에 오류가 없었다. 새 미추적 문서의 공백·링크 검사는 별도로 수행했다.
이는 문서와 변경 범위 확인이며 모델 성능 또는 노트북 실행 검증이 아니다.
