"""
LC 242 - Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Topics: HashMap, Sorting

Approach:
- Solution: 두 문자열을 정렬해서 비교
- SolutionCounter: Counter로 글자별 개수를 세서 비교 (dict 비교: 키와 개수가 모두 같은지)

Time / Space:
- Solution: O(N log N) / O(N)
- SolutionCounter: O(N) / O(K)  (K: 서로 다른 문자 수, 소문자만이면 O(1))

Edge cases:
- 길이가 다르면 False (Counter 비교 전에 길이 체크하면 더 빠름)

Takeaways:
- sorted(s)는 문자열을 바로 받아 리스트를 반환하므로 list() 불필요
- 비교식 결과가 이미 bool이라 if/else 없이 return 가능
- 개수 세기(Counter)는 정렬보다 빠르고, 유니코드 follow-up에도 그대로 쓸 수 있다

Revisit? N
"""

from collections import Counter
from typing import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)): return True
        else: return False


class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t): return True
        else: return False
