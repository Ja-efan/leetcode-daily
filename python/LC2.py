"""
LC 2 - Add Two Numbers 
Link: https://leetcode.com/problems/add-two-numbers/description/

Approach: pointer
- 

Time / Space: O(N) / O(N)
Edge cases: -
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 결과 리스트의 가짜 헤드 노드 
        dummy = ListNode()
        # 가짜 노드 포인터 
        current = dummy
        # 올림 수 
        carry = 0

        # 시작 노드 초기화 
        l1_curr = l1
        l2_curr = l2

        while l1_curr or l2_curr or carry:

            # 현재 노드 값 가져오기 (없으면 0)
            l1_val = l1_curr.val if l1_curr else 0
            l2_val = l2_curr.val if l2_curr else 0

            # 합산 및 올림 처리
            carry, digit = divmod(l1_val + l2_val + carry, 10)
            # 새 노드 생성 및 연결
            current.next = ListNode(digit)
            # 포인터 이동
            current = current.next
            
            # 다음 노드로 이동
            l1_curr = l1_curr.next if l1_curr else None
            l2_curr = l2_curr.next if l2_curr else None

        return dummy.next
