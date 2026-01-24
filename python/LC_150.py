"""
LC 150 - Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/

Approach: use a stack 
- 

Time / Space: O(N) / O()
Edge cases: -
- 

Takeaways: element 가 연산기호가 아닌 경우를 먼저 검사해주는 것이 훨씬 빠르다.
- 
Revisit? N
"""

from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = tokens[::-1]
        tmp = list()
        while stack:
            element = stack.pop()
            if element not in ["+", "-", "*", "/"]:
                tmp.append(int(element))
            else:
                a = int(tmp.pop())
                b = int(tmp.pop())
                if element == "+":
                    tmp.append(a + b)
                elif element == "-":
                    tmp.append(b-a)
                elif element == "*":
                    tmp.append(a * b)
                elif element == "/":
                    tmp.append(int(b / a))

        
        return tmp[0]