"""
LC 102 - Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Topics: Tree,BFS/DFS

Approach:
- deque 로 층 단위 BFS 를 한다. 한 층의 노드를 앞에서부터 꺼내며 값을 모으고, 자식을 left, right 순서로 다음 층 deque 에 넣는다.

Time / Space: O(N) / O(W)  (W: 트리의 최대 너비)

Edge cases:
- 빈 트리 -> []
- 노드 1개

Takeaways:
- 값의 순서를 지켜야 하면 스택이 아니라 큐(deque.popleft)로 층 단위 탐색을 한다.

Revisit? N
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[1:]
    i = 0
    for nd in nodes:
        if nd is None:
            continue
        if i < len(kids):
            nd.left = kids[i]; i += 1
        if i < len(kids):
            nd.right = kids[i]; i += 1
    return nodes[0]

from collections import deque 
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
            return[]
        current_stack = deque([])
        next_stack = deque([])
        
        result = list() 
        
        current_stack.append(root)
        while current_stack: 
            current_node_list = list() 
            while current_stack: 
                node = current_stack.popleft() 
                current_node_list.append(node.val)
                if node.left: 
                    next_stack.append(node.left)
                if node.right: 
                    next_stack.append(node.right)
            
            result.append(current_node_list)
            
            current_stack, next_stack = next_stack, deque([])
        
        return result


if __name__ == "__main__":
    cases = [
        ((build([3, 9, 20, None, None, 15, 7]),), [[3], [9, 20], [15, 7]]),
        ((build([1]),), [[1]]),
        ((build([]),), []),
    ]
    for args, expected in cases:
        got = Solution().levelOrder(*args)
        print("OK " if got == expected else "FAIL", args, got, expected)
