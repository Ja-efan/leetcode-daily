"""
LC 645 - Set Mismatch
Link: https://leetcode.com/problems/set-mismatch/

Approach: Hashmap 사용 

Time / Space: O(n) / O(n)
- 

Takeaways: 더 효율적인 접근이 있을 것 같다.
- 
Revisit? Y
"""

from typing import *

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        counter = Counter(nums)

        duplicate = 0
        missing = 0

        num_chk = [0 for _ in range(len(nums)+1)]
        num_chk[0] = 1
        for k, v in counter.items():
            if v > 1:
                duplicate = k        
            num_chk[k] = 1

        for i in range(len(num_chk)):
            if not num_chk[i]:
                missing = i 
        
        return [duplicate, missing]