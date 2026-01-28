"""
LC 20 - Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Approach: 
- Stack

Time / Space: O(N) / O(N)
"""

from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        push_list = ["(", "{", "["]
        match_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for s in s:
            if s in push_list: 
                stack.append(s)
            else: 
                if stack:
                    pop_element = stack.pop()
                    if match_map[s] == pop_element:
                        continue 
                    else:
                        return False 
                else:
                    return False
        if not stack:
            return True
        else: 
            return False
