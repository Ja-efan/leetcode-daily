"""
LC 344 - Reverse String
Link: https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Topics: Two Pointers,String

Approach:
- 양 끝에 포인터 l, r 을 두고 안쪽으로 좁히며, 값이 다르면 임시 변수로 교환했다.

Time / Space: O(n) / O(1)

Edge cases:
- 길이 1이거나 홀수 길이일 때 가운데 원소는 l < r 조건으로 건드리지 않음
- 양 끝 값이 같으면 교환 없이 넘어감

Takeaways:
- 양 끝 포인터를 안쪽으로 좁히며 서로 다른 값이면 임시 변수로 교환했다

Revisit? N
"""

from typing import *


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = None

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp
                l += 1
                r -= 1


if __name__ == "__main__":
    cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]
    for arg, expected in cases:
        s = list(arg)
        Solution().reverseString(s)
        print("OK " if s == expected else "FAIL ", arg, s, expected)
