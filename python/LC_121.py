"""
LC 121 - Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Topics: Array, Sliding Window

Approach:
- 가격 배열을 한 번 순회하면서 지금까지의 최저가를 갱신하고, 오늘 팔았을 때의 이익으로 최대 이익을 갱신한다.

Time / Space: O(N) / O(1)

Edge cases:
- 계속 하락하는 경우 -> 0

Takeaways:
- 최저가를 들고 한 번 순회하면 O(N)

Revisit? N
"""

from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit   


if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([7, 1, 5, 3, 6, 4],), 5),
        (([7, 6, 4, 3, 1],), 0),
    ]
    for args, expected in cases:
        result = sol.maxProfit(*args)
        print("OK " if result == expected else "FAIL", args, "->", result, "expected", expected)
