"""
LC 155 - Min Stack
Link: https://leetcode.com/problems/min-stack/
Difficulty: Medium
Topics: Stack

Approach:
- MinStackTwoStacks: 값 스택과 "각 원소가 들어오는 시점의 최솟값" 스택을 나란히 두고 같이 push/pop 한다.
- MinStack: 스택 하나에 (값, 그 시점의 최솟값) 튜플을 넣는다.

Time / Space: O(1) (모든 연산) / O(N)

Edge cases:
- pop, top, getMin 은 비어 있지 않은 스택에서만 호출된다.

Takeaways:
- 원소를 넣을 때 그 시점의 최솟값을 함께 저장하면 getMin 이 O(1)

Revisit? N
"""

from typing import *

class MinStackTwoStacks:
    def __init__(self):
        self.stack = list()
        self.min_values = list()  # 각 원소가 들어오는 시점의 최솟값을 저장할 수 있도록 한다.

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_values: self.min_values.append(value)
        else:
            self.min_values.append(min(value, self.min_values[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


class MinStack:
    # pop, top, getMin 3개의 method 는 non-empty 상태의 stack 에서만 동작한다. 
    def __init__(self):
        self.stack = list() 

    def push(self, value: int) -> None:
        if not self.stack: 
            self.stack.append((value, value))
        else: 
            min_value = min(self.stack[-1][1], value)
            self.stack.append((value, min_value))
        
    def pop(self) -> None:
        self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1][0] 

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    params = [[],[-2],[0],[-3],[],[],[],[]]
    expected = [None,None,None,None,-3,None,0,-2]
    obj = None
    for op, p, exp in zip(ops, params, expected):
        if op == "MinStack":
            obj = MinStack(*p)
            got = None
        else:
            got = getattr(obj, op)(*p)
        print("OK " if got == exp else "FAIL", op, p, got, exp)
