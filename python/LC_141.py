"""
LC 141 - Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Topics: Linked List, Two Pointers

Approach:
- slow 는 한 칸, fast 는 두 칸씩 이동한다. 사이클이 있으면 둘이 같은 노드에서 만나고, 없으면 fast 가 끝(None)에 도달한다.

Time / Space: O(N) / O(1)

Edge cases:
- 빈 리스트, 노드 1개
- 마지막 노드가 첫 노드로 연결된 경우

Takeaways:
- 속도가 다른 두 포인터로 사이클을 O(1) 공간에 찾는다.

Revisit? N
"""

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head 
        fast = head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast: 
                return True 
        return False            


def build(values, pos):
    # values 로 연결 리스트를 만들고, pos 가 -1 이 아니면 마지막 노드를 pos 번째 노드에 연결한다.
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    cases = [
        (([3, 2, 0, -4], 1), True),
        (([1, 2], 0), True),
        (([1], -1), False),
        (([None], -1), False),
        
    ]
    for (values, pos), expected in cases:
        got = Solution().hasCycle(build(values, pos))
        print("OK " if got == expected else "FAIL", values, pos, got, expected)
