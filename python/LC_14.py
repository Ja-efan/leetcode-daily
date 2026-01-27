"""
LC 14 - Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Approach: Brute Force
- 

Time / Space: O(MN) / O(NM)
"""

from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        result = ""

        for i in range(min_length):
            sett = {s[i] for s in strs}
            if len(sett) == 1:
                result += list(sett)[0]
            else: break
        return result