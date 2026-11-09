"""
LC 1046 - Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/
Difficulty: Easy
Topics: Heap

Approach:
- heapq 는 최소 힙이므로 돌 무게에 -를 붙여 최대 힙처럼 사용한다.
- 가장 무거운 두 돌 x >= y 를 꺼내 x != y 이면 x - y 를 다시 넣는다. 돌이 하나 남으면 그 무게를, 없으면 0 을 반환한다.

Time / Space: O(N log N) / O(N)

Edge cases:
- 돌이 하나뿐인 경우
- 모든 돌이 사라져 0 인 경우

Takeaways:
- 최대 힙은 부호를 뒤집은 최소 힙으로 구현한다.

Revisit? N
"""

from typing import *
import heapq 

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 가장 무거운 돌 두개를 꺼내어서 충돌 시킨다. 
        # 이때 충돌한 두 돌의 무게에 따라 분기된다. 
        # 두 돌의 무게를 각각 x, y 라고 가정했을 때, x == y 인 경우 두 돌은 모두 사라진다. 
        # 하지만 하나의 돌이 더 무거운 경우 x > y or x < y 인 경우 |x-y| 무게를 가지는 새로운 돌이 남게 된다. 
        # 모든 돌을 가능할 때 까지 충돌시킨다고 했을 때, 마지막에 남는 돌의 무게를 구한다. 
        # 남는 돌이 없다면 0 을 반환한다. 
        
        # 결국 리스트에서 가장 무거운 돌 두개를 꺼내는게 가장 중요한 로직이겠다. 
        
                    
        # stones 배열에서 가장 무거운 두 개의 돌을 꺼낸다. 
        # heapq 로 만들어지는 heap 은 min heap 이기 때문에 음수로 변환해서 저장한다. 
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while heap: 
        
            # 종료 조건 1 
            if len(heap) == 1: 
                return -heap[0]

            
            # x >= y 가 항상 성립 
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            
            if x != y: 
                
                heapq.heappush(heap, -(x-y))
        
        # 종료 조건 2
        return 0 


if __name__ == "__main__":
    cases = [
        (([2,7,4,1,8,1],), 1),
        (([1],), 1),
    ]
    for args, expected in cases:
        got = Solution().lastStoneWeight(*args)
        print("OK " if got == expected else "FAIL", args, got, expected)
