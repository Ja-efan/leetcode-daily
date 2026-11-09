"""
LC 1 - Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topics: HashMap, Array

Approach:
- Solution: 이중 for 문으로 모든 쌍을 확인 (브루트포스)
- SolutionRevisit: 값 -> 인덱스 리스트 해시맵을 먼저 만들고, 순회하며 target - x 를 조회. 같은 숫자 두 개는 x * 2 == target 일 때 따로 처리

Time / Space:
- Solution: O(N^2) / O(1)
- SolutionRevisit: O(N) / O(N)

Edge cases:
- 같은 숫자 두 개로 target 을 만드는 경우 ([3, 3], target 6)

Takeaways:
- 해시맵 조회로 짝을 찾으면 O(N)

Revisit? N
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두 개씩 더해서 target 과 같은 경우를 찾는다.
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    

from collections import defaultdict
class SolutionRevisit:
    def two_sum(self, nums: List[int], target: int) -> List[int]:    
        # nums 에서 두 개의 숫자 뽑아 target 이 되는 두 숫자의 index 를 반환한다. 
        
        # key: value = num: index 형식의 dict(hashmap) 을 구성한다. 
        # nums 를 1회 순회하며 각 숫자별로 hashmap 을 1번씩 search 한다. 
        
        n = len(nums)
        hashmap = defaultdict(list)
        for index in range(n):
            hashmap[nums[index]].append(index)
        # hashmap = {nums[index]: index for index in range(n)}
        
        for i in range(n):
            x = nums[i]
            if x * 2 == target and len(hashmap[x]) == 2:
                return hashmap[target-x]
            
            if x * 2 != target and target - x in hashmap.keys():
                return [i, hashmap[target-x][0]]            
    
        
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
