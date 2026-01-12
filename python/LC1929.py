"""
LC 1929 - Concatenation of Array
Link: https://leetcode.com/problems/concatenation-of-array/

Approach: 두 리스트를 + 연산자로 합친다.
- 

Time / Space: O(n) / O(n)
Edge cases: -
- 

Takeaways: 리스트를 대상으로 + 연산을 하는 경우 nums 의 원소 n 개를 복사해서 새 리스트(길이 2n) 를 만들어야 해서 시간 복잡도는 O(n) 이다.
- 
Revisit? N
"""

from typing import *

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums