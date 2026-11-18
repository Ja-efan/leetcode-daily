"""
LC 1971 - Find if Path Exists in Graph
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Difficulty: Easy
Topics: BFS/DFS

Approach:
- edges로 양방향 인접 리스트를 만들고, 스택(반복 DFS)과 visited 집합으로 source에서 destination까지 탐색한다.

Time / Space: O(V + E) / O(V + E)

Edge cases:
- source == destination이면 바로 True
- 간선이 없는 그래프 (n=1)
- source와 destination이 서로 다른 연결 요소에 있는 경우

Takeaways:
- 인접 리스트와 스택 DFS로 source에서 갈 수 있는 노드를 탐색한다

Revisit? N
"""

from typing import *


from collections import defaultdict 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        if source == destination: 
            return True
        for edge in edges: 
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        
        stack = [source]
        visited.add(source)
        while stack: 
            node = stack.pop() 
            for v in graph[node]:
                if v == destination:
                    return True 
                if v in visited: 
                    continue 
                stack.append(v)
                visited.add(v)
        return False
                
                
                
        


if __name__ == "__main__":
    cases = [
        ((3, [[0, 1], [1, 2], [2, 0]], 0, 2), True),
        ((6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False),
        ((1, [], 0, 0), True),
        ((10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5), True)
    ]
    for args, expected in cases:
        got = Solution().validPath(*args)
        print("OK " if got == expected else "FAIL", args, "->", got, "expected", expected)
