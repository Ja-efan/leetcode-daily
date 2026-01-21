"""
LC 1475 - Final Prices With a Special Discount in a Shop
Link: https://leetcode.com/problems/

Approach: stack 
- 

Time / Space: O(N) / O(N)
Edge cases:
- 

Takeaways: Monotonic stack 이라는 개념을 찾아봐야 할 것 같다.
"""

from typing import *

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # # O(N^2)
        # result = list()
        # for i in range(len(prices)):
        #     price = prices[i]
        #     if i == len(prices)-1:
        #         result.append(price)
        #         break
        #     for j in range(i+1, len(prices)):
        #         if price >= prices[j]:
        #             result.append(price - prices[j])
        #             break
        #     else:
        #         result.append(price)
        

        # O(N)
        stack = list()  # 할인 받지 못한 물건의 인덱스를 저장 
        result = prices[:]  # 할인 가격 담는 결과 리스트 

        for i, price in enumerate(prices):

            # 할인 받을 물건이 존재하면서, 해당 가격이 현재 물건의 가격 이상인 경우 
            # stack 에서 물건을 꺼내서 할인을 적용한다. 
            while stack and prices[stack[-1]] >= price: 
                popped_index = stack.pop()
                result[popped_index] -= price 
            # 현재 물건(아직 할인 못받음)을 stack 에 push
            stack.append(i)
        
        return result