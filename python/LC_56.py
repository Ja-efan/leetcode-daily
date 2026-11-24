"""
LC 56 - Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium
Topics: Array

Approach:
- 시작점 기준 내림차순 정렬 후 pop()으로 가장 빠른 구간부터 꺼내, results 의 마지막 구간과 겹치면 end 를 max 로 갱신하고 아니면 새로 추가한다.

Time / Space: O(n log n) / O(n)

Edge cases:
- 끝점과 시작점이 맞닿는 구간 ([1,4], [4,5])
- 입력이 정렬되어 있지 않은 경우 ([4,7], [1,4])

Takeaways:
- 시작점 기준으로 정렬한 뒤 마지막 병합 구간의 end 와 비교해 병합했다.

Revisit? N
"""
from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0], reverse=True)
        n = len(intervals)
        
        # 병합 된 구간 리스트 
        results = [intervals[-1]] # 첫 구간으로 초기화 
        
        # results 의 마지막 구간과 intervals 의 가장 빠른 구간을 비교해서 병합/저장.
        interval = intervals[:-1]
        while intervals:
            # results 의 마지막 구간 
            last_start, last_end = results[-1]
            
            # intervals 의 가장 빠른 구간 
            interval = intervals.pop() 
            interval_start = interval[0]
            interval_end = interval[1]
            
            # 두 구간 비교 
            # # interval_start 가 last_end 보다 큰 경우 두 구간을 병합한다. 
            # # 병합 시에는 last_end 와 interval_end 중 큰 값으로 구간의 end 를 지정한다.
            if last_end >= interval_start:
                results[-1][1] = max(last_end, interval_end)
                
            else: 
                results.append(interval)
        
        return results


if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([[1,3],[2,6],[8,10],[15,18]],), [[1,6],[8,10],[15,18]]),
        (([[1,4],[4,5]],), [[1,5]]),
        (([[4,7],[1,4]],), [[1,7]]),
    ]
    for args, expected in cases:
        got = sol.merge(*args)
        print("OK " if got == expected else "FAIL", args, got, expected)
