"""
LC 136 - Single Number
Link: https://leetcode.com/problems/single-number/
Difficulty: Easy
Topics: Array, Bit Manipulation

Approach:
- Sol 1: Counter로 값별 등장 횟수를 세고, 1번 나온 값을 반환
- Sol 2: 0에서 시작해 모든 원소를 XOR로 누적. 두 번 나온 값은 x ^ x = 0으로 지워지고 한 번 나온 값만 남는다

Time / Space:
- Sol 1: O(n) / O(n)
- Sol 2: O(n) / O(1)

Edge cases:
- 원소가 하나뿐인 경우 ([1])

Takeaways:
- 모든 원소를 XOR로 누적해 짝을 지우고 남은 값을 반환했다

Revisit? Y
"""
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 한 번만 나오는 원소를 반환한다. (나머지는 모두 두 번씩 나온다)
        # 조건: 시간 O(n), 추가 공간 O(1)

        # Sol 1 - 시간 O(n), 공간 O(n): 서로 다른 값마다 Counter 키가 생긴다
        # from collections import Counter
        # c = Counter(nums)
        # for k in c.keys():
        #     if c[k] == 1:
        #         return k

        # Sol 2 - 시간 O(n), 공간 O(1)
        # x ^ x = 0, x ^ 0 = x 이고 순서를 바꿔도 결과가 같다
        # -> 두 번 나온 값은 서로 지워지고 한 번 나온 값만 남는다
        k = 0
        for n in nums:
            k ^= n

        return k


if __name__ == "__main__":
    cases = [
        (([2,2,1],), 1),
        (([4,1,2,1,2],), 4),
        (([1],), 1),
    ]
    for args, exp in cases:
        got = Solution().singleNumber(*args)
        print("OK " if got == exp else "FAIL ", args, got, exp)
