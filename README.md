# LeetCode Daily

1일 1리트코드 챌린지 기록 저장소  
목표: 하루 한 문제. 꾸준함. 기본기. 깔끔한 코드

## Rules
- 하루 최소 1문제 (Easy/Medium 위주, 가끔 Hard)
- 시간 제한: Easy 20분 / Medium 40분. 넘기면 힌트·풀이를 보고 **Revisit** 등록
- 풀이 후 반드시 **복기(Takeaways)** 1줄 이상 작성 (`-`로 비워두지 않기)
- 틀렸던 문제/시간 오래 걸린 문제는 **Revisit**로 재풀이
- 커밋 메시지 규칙: `<state>: LC-<id> <title> [Easy|Medium|Hard]`
  - state: `solved` 새 풀이 / `revisit` 재풀이 / `docs` 노트·로그 / `chore` 기타 정리

예) `solved: LC-1 Two Sum [Easy]`, `revisit: LC-645 Set Mismatch [Easy]`

## Structure
```
.
├── python/
│   ├── LC_1.py
│   └── …
├── notes/
│   ├── patterns.md
│   └── revisit.md
├── templates/
│   └── solution.py
└── log.md
```

## Daily Workflow
1. `cp templates/solution.py python/LC_<id>.py` 후 풀이
2. 파일 상단 템플릿(Approach, Time/Space, Edge cases, Takeaways, Revisit) 채우기
3. `log.md` Daily Log에 한 줄 추가 + Weekly Plan 체크 + Stats 갱신
4. Revisit 대상이면 `notes/revisit.md`에 등록
5. 커밋 (`solved: LC-<id> <title> [Difficulty]`)

## Log
- 진행 기록과 주간 계획은 `log.md`에 누적한다.

## Notes
- `notes/patterns.md`: 자주 나오는 패턴(투포인터, 슬라이딩윈도우, DP 등) 정리
- `notes/revisit.md`: 다시 풀 문제 목록 + 재풀이 날짜 + 개선점

## Problem Template
각 솔루션 파일 상단에 아래 포맷으로 남긴다. (`templates/solution.py`)

- Link:
- Approach:
- Time / Space:
- Edge cases:
- Takeaways:
- Revisit? Y/N

## Goals
- ~~1차 목표: 260112 - 260131 연속 스트릭 만들기~~ (16문제, 2026-02-02 중단)
- 2차 목표 (2026-11-01 ~ 2026-11-30)
  - 연속 스트릭 유지 (코딩테스트 대비)
  - 주요 패턴 5개 이상 `notes/patterns.md`에 정리
