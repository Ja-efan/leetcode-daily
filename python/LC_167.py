"""
LC 167 - Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium
Topics: Two Pointers, Array

Approach:
- 정렬된 배열이므로 양 끝에서 시작하는 두 포인터
- 합 > target 이면 right 를 줄이고, 합 < target 이면 left 를 올린다.
- 반환 인덱스는 1-indexed 라서 +1
- target 이 음수이면 부호를 뒤집고 배열을 reverse 해서 처리했다. (인덱스 변환 필요)

Time / Space: O(N) / O(1)  (음수 target 변환 시 배열 복사로 공간 O(N))

Edge cases:
- 음수 target, 음수/0 이 섞인 배열
- 원소 2개

Takeaways:
- 정렬된 배열에서 합을 찾을 때는 양 끝 두 포인터로 O(N)에 탐색할 수 있다.

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
        
        
