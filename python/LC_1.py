from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두 개씩 더해서 target 과 같은 경우를 찾는다.
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
