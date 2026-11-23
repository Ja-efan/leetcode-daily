"""
LC 543 - Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Difficulty: Easy
Topics: Tree,BFS/DFS

Approach:
- 재귀로 각 노드의 높이를 구하면서, 노드마다 left + right 의 최댓값을 지름으로 갱신한다.

Time / Space: O(n) / O(h)

Edge cases:
- 빈 노드는 높이 0으로 처리한다.
- 지름이 루트를 지나지 않을 수 있어 모든 노드에서 갱신한다.

Takeaways:
- 높이를 반환하며 노드마다 left + right 로 지름을 갱신했다.

Revisit? Y
"""
from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


class Solution:
    def __init__(self, ):
        self.height = 0 
    
    def get_height(self, node: Optional[TreeNode]):
        # base case - leaf node 인 경우 
        if not node: 
            return 0 
        
        # 양쪽의 자식 노드의 height 를 가져옴 
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        
        # 현재 node 를 기준으로 양쪽으로 뻗은 경로가 height 보다 큰 경우 최댓값 갱신
        if left + right > self.height:
            self.height = left + right 
        
        # 현재 노드의 height 반환 (더 큰쪽 +1)
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.get_height(root)
        return self.height
        
            


if __name__ == "__main__":
    cases = [
        (([1, 2, 3, 4, 5],), 3),
        (([1, 2],), 1),
    ]
    for args, expected in cases:
        got = Solution().diameterOfBinaryTree(build(*args))
        print("OK " if got == expected else "FAIL ", args, got, expected)
