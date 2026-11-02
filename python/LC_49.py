"""
LC 49 - Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topics: HashMap, Sorting, String

Approach:
- 각 문자열을 정렬한 결과를 key로 쓰는 defaultdict(list)에 원본을 모은다.
- 애너그램끼리는 정렬 결과가 같다.

Time / Space: O(N * K log K) / O(N * K)  (N: 문자열 수, K: 문자열 최대 길이)

Edge cases:
- 빈 문자열 "" -> key "" 로 묶인다
- 문자열 1개 -> [[s]]

Takeaways:
- "같은 것끼리 묶기"는 정규화한 값을 key로 하는 해시맵.
- 정렬 대신 알파벳 개수 튜플(26칸)을 key로 쓰면 O(N * K)로 줄일 수 있다.

Revisit? N
"""

from collections import defaultdict
from typing import *


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            results[key].append(s)

        return list(results.values())
