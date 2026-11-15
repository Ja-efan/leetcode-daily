"""
LC 746 - Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Difficulty: Easy
Topics: DP

Approach:
- dp[i] = i 번째 계단을 밟고 서 있을 때까지의 최소 비용 = min(dp[i-1], dp[i-2]) + cost[i]. 기저 dp[0] = cost[0], dp[1] = cost[1]
- 꼭대기는 마지막 계단 다음 칸이므로 답은 min(dp[-1], dp[-2])

Time / Space: O(N) / O(N)

Edge cases:
- 계단이 2개인 경우

Takeaways:
- 점화식에 비용을 더해서 최소 비용을 구하는 DP 테이블을 채운다.

Revisit? N
"""

from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """ 
        DP - 점화식 
        가장 꼭대기(index cost.length) 까지 도달하기 위한 최소 비용 구하기 
        계단은 한 번에 한 칸 혹은 두 칸 이동 가능 
        시작은 index 0 혹은 1 부터 시작 가능하다. 
        
        i 번째 계단에 도달하기 까지의 최소 비용 = min(i-1, i-2)
        즉, dp 리스트를 만들어 min(dp[cost.length-1], dp[cost.length-2])
        base cases 
        i = 0 -> cost[0]
        i = 1 -> min(cost[0], cost[1])
        
        """ 
        
        dp = [0 for _ in range(len(cost))]
        
        # base cases 
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        # print(dp)
        return min(dp[-1], dp[-2])


if __name__ == "__main__":
    cases = [(([10,15,20],), 15), (([1,100,1,1,1,100,1,1,100,1],), 6)]
    for args, expected in cases:
        got = Solution().minCostClimbingStairs(*args)
        print(("OK " if got == expected else "FAIL "), args, got, expected)
