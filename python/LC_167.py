"""
LC 167 - Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium
Topics: Two Pointers, Array

Approach:
- 

Time / Space: O() / O()

Edge cases:
- 

Takeaways:
- 

Revisit? N
"""

from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers (1-indexed 이기 때문에 최종 포인터에서 +1 한 값을 반환한다.)
        left, right = 0, len(numbers) - 1
        while left < right: 
            # 두 포인터의 합 == target 이면 포인터 위치를 반환한다.
            if numbers[left] + numbers[right] == target: 
                return [left + 1, right + 1]
            # 두 포인터의 합 > target 이면 우측 포인터를 좌측으로 한 칸 이동한다.
            elif numbers[left] + numbers[right] > target: 
                right -= 1 
            # 두 포인터의 합 < target 이면 좌측 포인터를 우측으로 한 칸 이동한다.
            else: 
                left += 1
                
                
        


if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([2, 7, 11, 15], 9), [1, 2]),
        (([2, 3, 4], 6), [1, 3]),
        (([-1, 0], -1), [1, 2]),
    ]
    for (numbers, target), expected in cases:
        result = sol.twoSum(numbers, target)
        print("OK " if result == expected else "FAIL", numbers, target, "->", result, "expected", expected)
        
        
