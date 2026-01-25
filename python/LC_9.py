"""
LC 9 - Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Approach: 문자열 비교 
- 

Time / Space: O(N) / O(N)
Edge cases: -
- 

Takeaways: -
- 
"""

from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        return False