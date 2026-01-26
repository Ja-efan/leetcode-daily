"""
LC 13 - Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/

Approach:
- Hashmap

Time / Space: O(n) / O(1)
Edge cases:
- 

Takeaways:
- 
"""

from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for i in range(len(s)):
            curr_value = roman_to_int[s[i]]
            if curr_value > prev_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            prev_value = curr_value
        return total