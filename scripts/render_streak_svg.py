#!/usr/bin/env python3
"""streak.py 의 JSON 을 읽어 README용 터미널 스타일 스트릭 SVG 를 만든다.

사용: python3 scripts/streak.py | python3 scripts/render_streak_svg.py assets/readme/streak.svg
텍스트는 한글 폰트 의존을 피하려고 영문/숫자만 쓴다.
"""
import json, sys, os
from datetime import date, timedelta

BG, FG, MUTED, LINE = "#1A1A1A", "#EFF1F6", "#8A8F98", "#2E2E2E"
ORANGE, ORANGE_DK = "#FFA116", "#7A4E0A"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

data = json.load(sys.stdin)
out = sys.argv[1] if len(sys.argv) > 1 else "streak.svg"

today = date.fromisoformat(data["today"])
cnt = {date.fromisoformat(k): v for k, v in data["days"].items()}
days = sorted(cnt)
N = len(days)
season = date.fromisoformat(data["season_start"])
cur = data["current_streak"]
run = {today - timedelta(i) for i in range(cur)} if cnt.get(today) else {today - timedelta(1 + i) for i in range(cur)}


def state(d):
    if cnt.get(d, 0) > 0: return "run" if d in run else "solved"
    if d < season: return "pre"
    return "today" if d == today else "missed"


def t(x, y, s, size, fill=FG, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{s}</text>')


W, H = 1200, 400
alt = (f'LeetCode streak: {cur} days current, {data["best_streak"]} best, '
       f'{data["active_days"]} of {N} recent days solved')
b = [f'<rect x="0" y="0" width="{W}" height="60" rx="24" fill="#242424"/><rect x="0" y="30" width="{W}" height="30" fill="#242424"/>']
for i, c in enumerate(("#FF5F57", "#FEBC2E", "#28C840")):
    b.append(f'<circle cx="{40+i*30}" cy="30" r="9" fill="{c}"/>')
b.append(t(W / 2, 37, "leetcode-daily — streak", 20, MUTED, 500, "middle"))
L = 64
b.append(t(L, 118, "$", 24, ORANGE, 700) + t(L + 36, 118, f"git log --grep=^solved --since={data['window_start']}", 24, FG, 500))
b.append(t(L, 190, "streak", 24, MUTED, 500) + t(L + 140, 190, f"{cur} days", 24, ORANGE, 800))
sw, gap, sx, sy = 24, 6, L + 140, 218
for i, d in enumerate(days):
    x = sx + i * (sw + gap)
    s = state(d)
    if s == "run": f = f'fill="{ORANGE}"'
    elif s == "solved": f = f'fill="{ORANGE_DK}"'
    elif s == "pre": f = f'fill="{LINE}"'
    elif s == "missed": f = f'fill="none" stroke="{MUTED}" stroke-width="2"'
    else: f = f'fill="none" stroke="{FG}" stroke-width="2"'
    b.append(f'<rect x="{x}" y="{sy}" width="{sw}" height="32" rx="6" {f}/>')
end = sx + N * (sw + gap) - gap
b.append(t(sx, sy + 62, f"{days[0]:%m/%d}", 18, MUTED) + t(end, sy + 62, f"{days[-1]:%m/%d}", 18, MUTED, anchor="end"))
b.append(t(L, 330, "best", 24, MUTED) + t(L + 140, 330, f'{data["best_streak"]}', 24, FG, 700)
         + t(L + 260, 330, "active", 24, MUTED) + t(L + 400, 330, f'{data["active_days"]}/{N}', 24, FG, 700)
         + t(L + 540, 330, "missed", 24, MUTED) + t(L + 680, 330, str(len(data["missed_days"])), 24, FG, 700))
b.append(t(L, 372, "$", 24, ORANGE, 700) + f'<rect x="{L+36}" y="353" width="14" height="26" fill="{FG}"/>')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
       f'aria-label="{alt}"><title>{alt}</title><rect width="{W}" height="{H}" rx="24" fill="{BG}"/>{"".join(b)}</svg>')
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
open(out, "w").write(svg)
print(out)
