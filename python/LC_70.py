"""
LC 70 - Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Topics: DP

Approach:
- 점화식 s(n) = s(n-1) + s(n-2) 로 배열(DP 테이블)을 채운다. 기저 s(1) = 1, s(2) = 2

Time / Space: O(N) / O(N)

Edge cases:
- n = 1, n = 2

Takeaways:
- n 번째 값은 앞의 두 값으로 구하는 점화식으로 DP 테이블을 채운다.

Revisit? N
"""

from typing import *


class Solution:
    def climbStairs(self, n: int) -> int:
        # n 칸의 계단을 오르는 방법의 개수를 센다.
        # 계단은 한 번에 1칸 혹은 2칸씩 오를 수 있다. 
        # n 번째 계단을 오르는 방법은 이전 칸(n-1)에서 한 칸 올라오는 방법 1가지와 
        # 두 칸 전(n-2)에서 두 칸 올라오는 방법이 있다. 
        # 즉, s(n) = s(n-1) + s(n-2) 라는 점화식이 세워진다.
        
        stairs = [0 for _ in range(n+1)] 
        # base cases 
        stairs[1] = 1 # 1
        if n == 1:  # early return 
            return 1 
        stairs[2] = 2 # 1+1 / 2 
        if n == 2: 
            return 2 
        
        for i in range(3, n+1): 
            stairs[i] = stairs[i-1] + stairs[i-2]
        
        return stairs[n]
            


if __name__ == "__main__":
    cases = [((2,), 2), ((3,), 3), ((4,), 5)]
    for args, expected in cases:
        got = Solution().climbStairs(*args)
        print(("OK " if got == expected else "FAIL "), args, got, expected)

