"""
LC 322 - Coin Change
Link: https://leetcode.com/problems/coin-change/
Difficulty: Medium
Topics: DP

Approach:
- dp[i] = 금액 i를 만드는 최소 동전 수. 마지막에 쓸 동전을 고정해 dp[i] = min(dp[i - coin] + 1)로 채운다.

Time / Space: O(len(coins) * amount) / O(amount)

Edge cases:
- amount = 0 이면 0
- 만들 수 없는 금액(dp가 inf로 남음)은 -1

Takeaways:
- 마지막 동전을 고정하고 dp[i - coin] + 1 의 최솟값으로 dp 테이블을 채웠다

Revisit? N
"""
from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        # DP 
        dp = [inf for _ in range(amount+1)]
        dp[0] = 0 
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin > i: continue 
                
                # i 가 coin 보다 크거나 같은 경우 해당 코인을 마지막 코인으로 고정한 경우의 수를 구할 수 있다. 
                # 마지막 코인으로 고정한 경우는 dp[i-coin] + 1 을 dp[i] 와 비교해서 작은 값을 채운다. 
                dp[i] = min(dp[i], dp[i-coin]+1)
                
        return dp[amount] if dp[amount] != inf else -1

if __name__ == "__main__":
    s = Solution()
    cases = [(([1,2,5], 11), 3), (([2], 3), -1), (([1], 0), 0)]
    for args, exp in cases:
        got = s.coinChange(*args)
        print("OK " if got == exp else "FAIL", args, got, exp)


"""

coins = [1, 3, 4], amount=6 

1 3 4 
0 2 0 

output = 2 


amount = 1 
1 3 4 
1 0 0 
output = 1 

amount = 2 
1 3 4 
2 0 0 
output = 2

amount = 3 
1 3 4 
0 1 0 
output = 1 

amout = 4 
1 3 4 
0 0 1 
output = 1 

amount = 5
1 3 4 
1 0 1 
output = 2 

amount = 6
1 3 4 
0 2 0 
output = 2
"""

# 마지막에 사용할 동전을 고정시킨 뒤, 
# amount - last_coin 을 한 금액에 해당하는 output에 1을 더한 값 중에 최솟값이 amount를 구성하기 위한 최소한의 동전 개수이다.