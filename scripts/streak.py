#!/usr/bin/env python3
"""git 커밋 기록에서 LeetCode 풀이 스트릭을 계산한다.

- 대상 커밋: 제목이 `solved:` 로 시작하는 커밋 (--include-revisit 이면 `revisit:` 도 포함)
- 날짜 기준: author date, KST(Asia/Seoul)
- 하루에 몇 문제를 풀어도 1일로 계산한다.
- 표시 창: 오늘 포함 최근 N일(롤링). 스트릭/최장 기록은 창과 무관하게 전체 기록으로 계산한다.
- 현재 스트릭: 오늘 또는 어제까지 이어진 연속 일수 (오늘 아직 안 풀었어도 어제까지 이어졌다면 유지)
"""
import argparse, json, subprocess
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")


def solved_days(repo, include_revisit):
    out = subprocess.run(
        ["git", "-C", repo, "log", "--format=%aI|%s"],
        capture_output=True, text=True, check=True,
    ).stdout
    prefixes = ("solved:",) + (("revisit:",) if include_revisit else ())
    days = {}
    for line in out.splitlines():
        iso, _, subject = line.partition("|")
        if subject.strip().lower().startswith(prefixes):
            d = datetime.fromisoformat(iso).astimezone(KST).date()
            days[d] = days.get(d, 0) + 1
    return days


def streaks(days, today):
    ds = sorted(days)
    best, run, prev, best_end = 0, 0, None, None
    for d in ds:
        run = run + 1 if prev and d - prev == timedelta(1) else 1
        if run >= best:
            best, best_end = run, d
        prev = d
    cur, d = 0, today if today in days else today - timedelta(1)
    while d in days:
        cur += 1
        d -= timedelta(1)
    return cur, best, best_end


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--window", type=int, default=30, help="표시할 최근 일수 (오늘 포함)")
    ap.add_argument("--season-start", default="2026-11-01", help="이 날짜 이전의 빈 날은 놓친 날로 세지 않는다")
    ap.add_argument("--include-revisit", action="store_true")
    ap.add_argument("--today", help="테스트용 (YYYY-MM-DD)")
    a = ap.parse_args()

    today = date.fromisoformat(a.today) if a.today else datetime.now(KST).date()
    days = solved_days(a.repo, a.include_revisit)
    cur, best, best_end = streaks(days, today)
    season = date.fromisoformat(a.season_start)
    span = [today - timedelta(i) for i in range(a.window - 1, -1, -1)]
    result = {
        "today": today.isoformat(),
        "window": a.window,
        "season_start": a.season_start,
        "window_start": span[0].isoformat(),
        "current_streak": cur,
        "best_streak": best,
        "best_streak_end": best_end.isoformat() if best_end else None,
        "active_days": sum(1 for d in span if d in days),
        "missed_days": [d.isoformat() for d in span if d not in days and d != today and d >= season],
        "total_solved_days": len(days),
        "days": {d.isoformat(): days.get(d, 0) for d in span},
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
