"""
LC 448 - Find All Numbers Disappeared in an Array
e
Link: https://leetcode.com/problems/

Approach: Hash
- 

Time / Space: O(N) / O(N)
Edge cases:
- 

Takeaways: 
- 
Revisit? Y/N
"""

from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums_set = set(nums)

        result = list()
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                result.append(i)

        return result    