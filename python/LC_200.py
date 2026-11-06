"""
LC 200 - Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Topics: BFS/DFS

Approach:
- 격자를 순회하다 '1'이고 방문하지 않은 칸을 만나면 섬 개수를 +1 하고, BFS 로 연결된 칸을 모두 방문 처리한다.

Time / Space: O(R * C) / O(R * C)

Edge cases:
- 칸이 하나뿐인 섬
- 땅이 없는 경우

Takeaways:
- 탐색을 새로 시작하는 횟수가 섬의 개수

Revisit? N
"""

from typing import *
from collections import deque 


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # bfs 섬 개수 찾기 
        
        num_islands = 0 
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    num_islands += 1
                    
                    q = deque() 
                    q.append([i, j])
                    while q: 
                        sr, sc = q.popleft() 
                        for dr, dc in directions: 
                            nr, nc = sr + dr, sc + dc 
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append([nr, nc])
                    
        return num_islands
                
            
        


if __name__ == "__main__":
    cases = [
        (([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],), 1),
        (([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],), 3),
    ]
    for args, expected in cases:
        got = Solution().numIslands(*args)
        print("OK " if got == expected else "FAIL", args, got, expected)
