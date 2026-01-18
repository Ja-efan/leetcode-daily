"""
LC 1441 - Build an Array With Stack Operations

Link: https://leetcode.com/problems/

Approach: stack and set
- 

Time / Space: O(N) / O(N)
Edge cases: -
- 

Takeaways: - 
- 
Revisit? N
"""

from typing import *

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        result = []  # stack 
        target_set = set(target)
        operations = []

        stream = list(range(n, 0, -1))
        while True: 
            # result(stack)의 원소가 target 과 동일하면 아무런 연산을 하지말고 그대로 반환한다.
            if result == target: 
                break

            # stream 이 비어있지 않은 경우 stream의 다음 숫자를 result(stack) 에 push 한다.
            if stream:
                next_element = stream.pop()
                result.append(next_element)
                operations.append("Push")

            # result(stack) 이 비어있지 않으면 마지막 원소를 pop 할 수 있다.
            if next_element not in target_set:
                result.pop()
                operations.append("Pop")

        return operations