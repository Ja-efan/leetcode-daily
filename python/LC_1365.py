"""
LC id - How Many Numbers Are Smaller Than the Current Number
Link: https://leetcode.com/problems/

Approach: list, hashmap
- 

Time / Space: O(N) / O(N)
Edge cases: - 
- 

Takeaways: -
- 
Revisit? N
"""

from typing import *

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_cnt = [0 for _ in range(501)]

        for num in nums:
            num_cnt[num] += 1
        
        result = []
        for i in range(n):
            num = nums[i]
            result.append(sum(num_cnt[:num]))

        
        return result