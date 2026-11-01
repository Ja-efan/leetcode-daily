"""
LC 217 - Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topics: HashMap, Set

Approach:
- Solution: set에 넣으면서 순회, 이미 본 값이 나오면 바로 True (early exit)
- SolutionSetLen: set(nums)의 길이와 nums 길이 비교

Time / Space: O(N) / O(N) (두 풀이 동일)

Edge cases:
- 원소 1개 -> False
- 중복이 앞쪽에 있는 경우 -> Solution은 바로 종료, SolutionSetLen은 전체 set 생성

Takeaways:
- "이미 본 적 있나?"는 set 멤버십 체크(O(1))로 푼다.
- 한 줄 풀이는 간결하지만 항상 전체 set을 만든다. 순회 풀이는 중복을 찾는 즉시 종료할 수 있다.

Revisit? N
"""

from typing import *


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False


class SolutionSetLen:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(list(set(nums))) != len(nums): return True
        else: return False
