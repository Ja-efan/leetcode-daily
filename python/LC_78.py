"""
LC 78 - Subsets
Link: https://leetcode.com/problems/subsets/
Difficulty: Medium
Topics: Backtracking

Approach:
- itertools.combinations로 크기 1..n-1 조합을 만들어 이어 붙이고, 빈 집합과 전체 집합은 따로 넣는다.

Time / Space: O(n * 2^n) / O(n * 2^n) (보조 공간은 O(n))

Edge cases:
- n=1 (range(1, n)이 비어 빈 집합과 전체 집합만 반환)
- 빈 부분집합 포함

Takeaways:
- itertools.combinations로 크기별 조합을 만들어 모든 부분집합을 구했다.

Revisit? Y
"""

from typing import *


from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = list() 
        results.append([])
        results.append(nums)
        for i in range(1, n):
            comb = combinations(nums, i)
            
            results.extend(comb)
        
        # print(results)
        return results


if __name__ == "__main__":
    cases = [
        (([1,2,3],), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        (([0],), [[],[0]]),
    ]
    for args, expected in cases:
        got = Solution().subsets(*args)
        print("OK " if sorted(map(sorted, got or [])) == sorted(map(sorted, expected)) else "FAIL", got, expected)

