# 인계 — 자동 검사·학생 경로·대표 예제 재현

[팩트] 사용자가 승인한 CI → 학생 안내 기술 점검 → 대표 예제 새 환경 재현을 순서대로 진행했습니다. 공개 학생 데모와 공개 Iris 참조만 사용했습니다. 비공개 전략·모델·계정·실제 장치 접속은 수행하지 않았습니다.

## 학생용 데모

- 저장소: [quant-pi-trading-demo](https://github.com/Joon-Jeremy-Chun/quant-pi-trading-demo)
- 게시 확인: `14ba4beefb592614d2ca5350ccb11fbb5eea642b`, origin/main 일치.
- [자동 검사 설명](https://github.com/Joon-Jeremy-Chun/quant-pi-trading-demo/blob/main/docs/CI.md): Linux/Windows × Python 3.10/3.13 및 Node 22, 총 다섯 작업.
- [ZIP 점검 기록](https://github.com/Joon-Jeremy-Chun/quant-pi-trading-demo/blob/main/docs/STUDENT_CHECK.md): Git 없는 새 ZIP·서드파티 패키지 0개인 venv에서 CLI·과제 해설·문서·로컬 서버 경로를 확인했습니다.
- Git 없는 배포 경로를 publication checker가 지원하고, `verify_classroom.py --check`는 기존 증거를 덮어쓰지 않습니다. Python 25개·JS 9개 검사와 기존 공개 이력 민감 패턴 점검을 연결했습니다.
- 실제 학생 피드백은 미확인입니다. 에이전트의 기술 리허설로만 기록합니다.

## 대표 예제

- 저장소: [Machine_Learning_summary](https://github.com/Joon-Jeremy-Chun/Machine_Learning_summary)
- 구현 게시 확인: `6b7d4aa02f8c61103e4ff5b3be56589e4e47c5db`, origin/master 일치.
- [한글 재현 안내](https://github.com/Joon-Jeremy-Chun/Machine_Learning_summary/blob/master/docs/reproduction/random-forest/README.ko.md) · [영문 안내](https://github.com/Joon-Jeremy-Chun/Machine_Learning_summary/blob/master/docs/reproduction/random-forest/README.md)
- 기존 `Random_Forest.ipynb`의 코드와 원본 파일은 변경하지 않았습니다. 새 환경 두 개에서 실제 Jupyter 커널로 전체 실행했으며 고정 의존성 재설치 후에도 예측·분할 확인값이 같았습니다.
- 내장 Iris 자료의 기존 고정 분할은 학습 105개·평가 45개·인덱스 중복 0개입니다. 기존 설정에서 45개 중 42개 일치했고 virginica 세 개를 versicolor로 분류한 오류도 남겼습니다. 한 분할의 출력이며 성능 향상·모델 우수성을 뜻하지 않습니다.
- 실행 노트북·출력·환경/버전·예측 확인값·혼동행렬과 CRLF/LF를 구분한 해시 근거를 원본과 별도로 보존했습니다. 외부 데이터 노트북 전체 재현은 미확인입니다.

## 기록과 보존 경계

[팩트] 이번 범위는 기존 예제의 설치·실행·운영 검증입니다. 새 가설·모델 비교·튜닝을 수행하지 않았으며 공유 연구 기록 정책의 단순 기록 예외에 따라 저장소 로그와 인계로 묶었습니다. 원래 두 작업 폴더의 HEAD·Git 상태·33개 파일 해시는 시작 기준과 일치했습니다. 격리 worktree와 GitHub에 새 게시본을 남겼습니다.

## 게시와 hosted CI

[팩트] 학생 데모의 완료 기록 포함 최종 게시본 `14ba4beefb592614d2ca5350ccb11fbb5eea642b`에서 [run 40969967599](https://github.com/Joon-Jeremy-Chun/quant-pi-trading-demo/actions/runs/40969967599)의 다섯 작업이 모두 성공했습니다.

[팩트] Iris 구현 게시본 `6b7d4aa`의 [run 40969888400](https://github.com/Joon-Jeremy-Chun/Machine_Learning_summary/actions/runs/40969888400)에서 Linux/Windows 두 작업이 성공했습니다. 완료 기록 포함 최종 게시본 `a6e1c78f28d48063c2b8cb2968e31345fa88e288`도 원격 master와 일치했고, [후속 run 40970231483](https://github.com/Joon-Jeremy-Chun/Machine_Learning_summary/actions/runs/40970231483)의 두 작업까지 모두 성공했습니다. 최종 게시본 기준 총 일곱 hosted 작업의 성공을 확인했습니다.
