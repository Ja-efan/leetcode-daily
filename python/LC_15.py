"""
LC 15 - 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium
Topics: Two Pointers, Sorting, Array

Approach:
- 정렬 후 인덱스 i 를 고정하고, 나머지 둘은 양 끝 두 포인터로 탐색 (target = -nums[i])
- 합 > target 이면 right 를 줄이고, 합 < target 이면 left 를 올린다.
- 결과는 set 에 튜플로 저장해 중복을 제거하고, 고정 값이 이전 값과 같으면 건너뛴다.

Time / Space: O(N^2) / O(R)  (R: 결과 개수)

Edge cases:
- 모두 0 인 경우
- 중복 값이 많은 경우

Takeaways:
- 정렬 후 한 값을 고정하고 두 포인터로 탐색하면 O(N^2)

Revisit? N
"""

from itertools import combinations
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # approach : two pointers - 입력 배열 선 정렬 후 인덱스 하나 고정한 뒤 투 포인터로 양 끝에서 좁혀가며 게산. target 은 고정 인덱스 값*-1 로 계산.
        # 투 포인터 조건 : 현재 인덱스 값이 0 보다 작으면 왼쪽 포인터 이동, 0 보다 크면 오른쪽 포인터 이동.
        
        # 정렬 
        nums.sort()
        
        # 결과 배열 
        results = set()
        
        # 배열 순회 
        # i 는 고정 인덱스, nums[i] 는 고정 값, target = -nums[i] 로 계산 
        # i 는 마지막 인덱스 전까지 순회 -> 고정 인덱스 제외 두 개의 인덱스가 필요함. 
        for i in range(len(nums) - 2):
            # 중복 검사 - nums[i] 가 이전 값과 동일하면 건너뛴다. 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 투 포인터 초기화 
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            # 투 포인터 이동 조건 
            while left < right:
                # 현재 인덱스 값과 투 포인터 값 계산 
                current_sum = nums[left] + nums[right]
                # 현재 인덱스 값과 투 포인터 값 계산 
                if target == current_sum:
                    # 조건 충족 
                    results.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                # 합이 0보다 크면 오른쪽 포인터 좌측 이동 
                elif target < current_sum:
                    # 현재 인덱스 값과 투 포인터 값 계산 
                    right -= 1
                # 합이 0보다 작으면 왼쪽 포인터 우측 이동 
                else:
                    left += 1  

        return list(results)



def brute(nums: List[int]) -> List[List[int]]:
    # 정답 비교용 (O(N^3), 제출용 아님)
    nums = sorted(nums)
    return sorted([list(c) for c in {c for c in combinations(nums, 3) if sum(c) == 0}])


def normalize(result: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(t) for t in (result or []))


if __name__ == "__main__":
    import random

    sol = Solution()
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    for nums, expected in cases:
        result = sol.threeSum(list(nums))
        ok = normalize(result) == normalize(expected)
        print("OK " if ok else "FAIL", nums, "->", result, "expected", expected)

    # 랜덤 테스트: brute 와 비교
    bad = 0
    for _ in range(1000):
        nums = [random.randint(-5, 5) for _ in range(random.randint(3, 10))]
        result = sol.threeSum(list(nums))
        if normalize(result) != normalize(brute(nums)):
            bad += 1
            if bad <= 3:
                print("FAIL random", nums, "->", result, "expected", brute(nums))
    print("random test:", "OK" if bad == 0 else f"FAIL {bad}/1000")
