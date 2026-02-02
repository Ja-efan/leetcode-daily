"""
LC 21 - Merge Two Sorted Lists
Link: https://leetcode.com/problems/

Approach:
- 

Time / Space: O(N+M) / O(1)
- 

Takeaways:
- 
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None 

        # TODO: two pointer
        dummy = ListNode(0)  # 더미 헤더 생성 
        tail = dummy  # 더미로부터 시작
        p, q = list1, list2 

        while p and q:
            if p.val <= q.val:
                tail.next = p  # 다음 노드 갱신 
                p = p.next  # p 다음 노드로 갱신 
            else:
                tail.next = q  # 다음 노드 갱신 
                q = q.next  # q 다음 노드로 갱신 
            tail = tail.next  # tail 이동 (방금 업데이트 한 노드로)
        
        tail.next = p if p else q  # 마지막 노드 이어 붙이기

        return dummy.next 







        return result 
        