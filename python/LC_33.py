"""
LC 33 - Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium
Topics: Binary Search

Approach:
- mid 기준으로 left~mid 가 정렬됐는지 nums[left] <= nums[mid] 로 판별한다.
- 정렬된 쪽에 target 이 들어가면 그쪽으로, 아니면 반대쪽으로 범위를 좁힌다.

Time / Space: O(log n) / O(1)

Edge cases:
- left == mid (원소 1~2개 남은 구간) 에서 왼쪽을 정렬된 쪽으로 취급해야 한다. ([3,1], target 1)
- 원소가 하나인 배열, target 이 없는 경우

Takeaways:
- 정렬된 쪽을 먼저 판별한 뒤 그 구간 안에 target 이 있는지로 탐색 범위를 좁혔다.

Revisit? N
"""
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search 
        left, right = 0, len(nums)-1


        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 
            # mid 기준 left / right 이동 조건 
            
            # 왼쪽이 정렬된 경우 left.val < mid.val 
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # target 이 왼쪽 범위 안 -> right 을 mid-1로 수정 
                    right = mid -1
                else: # target 이 왼쪽 범위가 아님 -> 오른쪽으로 넘어가야함.
                    left = mid + 1
            # 오른쪽이 정렬된 경우 mid.val < right.val 
            else: 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid -1 
                
        return -1
            

if __name__ == "__main__":
    cases = [(([4,5,6,7,0,1,2], 0), 4), (([4,5,6,7,0,1,2], 3), -1), (([1], 0), -1), (([3,1], 1), 1)]
    for args, exp in cases:
        got = Solution().search(*args)
        print("OK " if got == exp else "FAIL ", args, got, exp)
