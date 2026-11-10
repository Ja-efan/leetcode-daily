"""
LC 645 - Set Mismatch
Link: https://leetcode.com/problems/set-mismatch/

Approach:
- Solution: Counter 로 개수를 세고, 1~n 체크 배열로 빠진 숫자를 찾는다.
- SolutionVer2: set 으로 중복 숫자를 찾고, 1~n 중 set 에 없는 숫자를 찾는다.

Time / Space:
- Solution: O(N) / O(N)
- SolutionVer2: O(N) / O(N)

Edge cases:
- 중복 숫자가 빠진 숫자보다 클 때와 작을 때 모두

Takeaways:
- set 으로 중복과 누락을 각각 찾을 수 있다.

Revisit? N
"""

from typing import *

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        counter = Counter(nums)

        duplicate = 0
        missing = 0

        num_chk = [0 for _ in range(len(nums)+1)]
        num_chk[0] = 1
        for k, v in counter.items():
            if v > 1:
                duplicate = k        
            num_chk[k] = 1

        for i in range(len(num_chk)):
            if not num_chk[i]:
                missing = i 
        
        return [duplicate, missing]
    
class SolutionVer2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 1-n 까지 정수가 들어있어야 하는 길이 n의 정수 리스트 nums 에 중복된 숫자 하나가 존재한다. 
        # 중복된 숫자 s 와 리스트에 들어있지 않은 숫자 m 를 구해 리스트로 반환한다. 
        
        n = len(nums)
        seen = set() 
        
        s = 0 
        m = 0
        
        # 중복(s) 탐지
        for num in nums: 
            if num in seen: 
                s = num
                continue 
            seen.add(num)
            
        # 놓침(m) 탐지 
        for i in range(1, n+1):
            if i not in seen: 
                m = i 
                break
            
        return [s, m]
    