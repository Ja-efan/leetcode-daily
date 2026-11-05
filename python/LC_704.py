"""
LC 704 - Binary Search
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy
Topics: Binary Search, Array

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
    def search(self, nums: List[int], target: int) -> int:
        # binary search 
        # 정렬된 배열에서 중간 값을 찾아 탐색한다. 
        # 중간 값이 타겟보다 크면 왼쪽 배열로 이동하고, 작으면 오른쪽 배열로 이동한다. 
        # 배열 중간 인덱스를 시작으로 한다. 
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target: # 오른쪽 배열로 이동, left = mid +1 
                left = mid + 1 
            else: # 왼쪽 배열로 이동, right= mid-1
                right = mid -1 
        return -1


if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1),
    ]
    for args, expected in cases:
        result = sol.search(*args)
        print("OK " if result == expected else "FAIL", args, "->", result, "expected", expected)
