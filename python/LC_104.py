"""
LC 104 - Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Topics: Tree,BFS/DFS

Approach:
- 스택 두 개(current_stack, next_stack)로 층별 탐색을 한다. 한 층을 모두 꺼내면서 자식을 next_stack 에 담고, 층이 바뀔 때마다 level 을 +1 한다.

Time / Space: O(N) / O(W)  (W: 트리의 최대 너비)

Edge cases:
- 빈 트리 -> 0
- 한쪽으로만 치우친 트리

Takeaways:
- 스택 두 개로 층 단위 탐색을 하면 층 수를 센다.

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
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for n in nodes:
        if n:
            if kids: n.left = kids.pop()
            if kids: n.right = kids.pop()
    return root


def to_list(root):
    out, q = [], [root]
    while q:
        n = q.pop(0)
        if n:
            out.append(n.val); q += [n.left, n.right]
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # stack 이용해서 층 개수를 센다. 
        if root is None: 
            return 0
        current_stack = list() 
        next_stack = list()
        
        current_stack.append(root)
        level = 0 
        
        while current_stack: 
            level += 1
            while current_stack: 
                current_node = current_stack.pop() 
                if current_node.left: 
                    next_stack.append(current_node.left)
                if current_node.right:
                    next_stack.append(current_node.right)
            current_stack, next_stack = next_stack, []
            
            
        return level 


if __name__ == "__main__":
    cases = [(([3,9,20,None,None,15,7],), 3), (([1,None,2],), 2), (([],), 0)]
    for args, exp in cases:
        got = Solution().maxDepth(build(args[0]))
        print("OK " if got == exp else "FAIL", args, got, exp)
