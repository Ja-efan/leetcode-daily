"""
LC 1470 - Shuffle the Array
Link: https://leetcode.com/problems/shuffle-the-array/description/

Approach: 입력으로 들어온 리스트를 슬라이싱해서 두 개의 리스트로 분할하고, 두 리스트에서 원소를 하나씩 꺼내서 결과 리스트에 추가.
- 

Time / Space: O(N) / O(N)
Edge cases: -  
- 

Takeaways: 리스트 슬라이싱은 항상 새 리스트를 복사해서 만든다. 즉, 새로운 리스트가 메모리에 할당된다.
- 
Revisit? N
"""

from typing import *

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        output = list()
        for a, b in zip(nums[:n//2], nums[n//2:]):
            output.extend([a,b])

        return output