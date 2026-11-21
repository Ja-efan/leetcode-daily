"""
LC 125 - Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Topics: Two Pointers,String

Approach:
- 소문자로 바꾼 뒤 정규식으로 영문자와 숫자만 남기고, 양 끝에서 두 포인터를 좁히며 비교한다.

Time / Space: O(n) / O(n)

Edge cases:
- 영숫자가 하나도 없는 입력(공백, 특수문자만)은 True
- alphanumeric 은 영문자와 숫자를 모두 포함하므로 숫자도 남긴다 ("0P" -> False)

Takeaways:
- 영숫자만 남긴 문자열을 양 끝 두 포인터로 비교한다.

Revisit? N
"""
from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 특수 문자를 모두 지우고, 모두 소문자로 변환한 뒤 palindrome 인지 확인 후 True/False 반환 
        # 특수문자 어떻게 지우지 - regex 
        import re 
        s = s.lower() 
        s = re.sub(r"[^a-z0-9]", "", s)
        # print(s)
        
        if len(s) == 0:
            # print('here')
            return True 
        # if len(s) == 1: 
        #     return False
        
        # 투포인터 ?
        left = 0
        right = len(s)-1
        while left < right:
            # print(s[left], s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            else: 
                return False 
        
        return True
                
        


if __name__ == "__main__":
    cases = [
        (("A man, a plan, a canal: Panama",), True),
        (("race a car",), False),
        ((" ",), True),
        (("0P",), False)
    ]
    for args, exp in cases:
        got = Solution().isPalindrome(*args)
        print("OK " if got == exp else "FAIL ", args, got, exp)
