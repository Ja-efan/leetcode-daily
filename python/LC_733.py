"""
LC 733 - Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Topics: BFS/DFS

Approach:
- 시작 칸의 원래 색(target_color)을 저장하고, 새 색과 같으면 바로 반환한다.
- 스택으로 상하좌우를 탐색하며 원래 색인 칸을 새 색으로 칠한다. 칠한 칸이 방문 표시 역할을 한다.

Time / Space: O(R * C) / O(R * C)

Edge cases:
- 새 색이 원래 색과 같은 경우
- 시작 칸과 이어지지 않은 같은 색 칸

Takeaways:
- 칠하는 것이 방문 표시를 대신하므로 visited 가 필요 없다.

Revisit? N
"""

from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # visited = set() 
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(image)
        n = len(image[0])
        
        stack = [(sr, sc)]
        
        target_color = image[sr][sc]
        if target_color == color:
            return image 
        image[sr][sc] = color        
        while stack: 
            r, c = stack.pop() # 현재 위치
            
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc # 다음 위치 후보 
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == target_color: # 유효성 검사 
                    image[nr][nc] = color 
                    stack.append((nr, nc))
            
        return image


if __name__ == "__main__":
    cases = [
        (([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]]),
        (([[0,0,0],[0,0,0]], 0, 0, 0), [[0,0,0],[0,0,0]]),
    ]
    for args, expected in cases:
        got = Solution().floodFill(*args)
        print("OK " if got == expected else "FAIL", got, expected)
