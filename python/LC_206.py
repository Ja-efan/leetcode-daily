"""
LC 206 - Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Topics: Linked List

Approach:
- prev, curr, nxt 세 포인터로 각 노드의 next 방향을 뒤집는다. (curr.next 를 nxt 에 저장 -> curr.next = prev -> prev, curr 이동)

Time / Space: O(N) / O(1)

Edge cases:
- 빈 리스트 -> None
- 노드 1개

Takeaways:
- 값이 아니라 next 화살표 방향을 뒤집는다.

Revisit? Y
"""
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head 가 tail 이 된다. 
        # linked list 의 화살표를 뒤집는다. 
        # 첫 노드의 방향을 뒤집는다. next.val 이 val 이 되고, val 은 next.val 이 된다. 
        # 이걸 언제까지 반복하는가 - 주어진 linked list 의 next 가 None 이 아닌 동안. 
        curr = head 
        prev = None
        nxt = None 
        
        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt   
        
        return prev
            
        
            


def build(a):
    d = ListNode()
    c = d
    for x in a:
        c.next = ListNode(x)
        c = c.next
    return d.next


def to_list(h):
    r = []
    while h:
        r.append(h.val)
        h = h.next
    return r


if __name__ == "__main__":
    cases = [(([1,2,3,4,5],), [5,4,3,2,1]), (([1,2],), [2,1]), (([],), [])]
    for args, exp in cases:
        got = to_list(Solution().reverseList(build(args[0])))
        print("OK " if got == exp else "FAIL", args, got, exp)
