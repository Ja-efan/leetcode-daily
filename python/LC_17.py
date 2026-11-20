"""
LC 17 - Letter Combinations of a Phone Number
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: Medium
Topics: Backtracking

Approach:
- 재귀 dfs(지금까지 만든 문자열, 자리 인덱스)로 자리마다 후보 글자를 붙여 내려간다.
- 문자열 길이가 len(digits)와 같아지면 results에 추가하고 return 한다.

Time / Space: O(n * 4^n) / O(n)  (n = len(digits), 공간은 출력 제외)

Edge cases:
- digits가 빈 문자열이면 [] 를 반환한다.

Takeaways:
- 자리마다 후보 글자를 붙이며 재귀 호출하고, 길이가 digits 길이와 같아지면 결과에 추가한다

Revisit? N
"""
from typing import *


class Solution:
    # from collections import defaultdict
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = dict()
        buttons[2] = ['a', 'b', 'c']
        buttons[3] = ['d', 'e', 'f']
        buttons[4] = ['g', 'h', 'i']
        buttons[5] = ['j', 'k', 'l']
        buttons[6] = ['m', 'n', 'o']
        buttons[7] = ['p', 'q', 'r', 's']
        buttons[8] = ['t', 'u', 'v']
        buttons[9] = ['w', 'x', 'y', 'z']
    
        n = len(digits)
        if n == 0:
            return []
        
        results = list() 
        def dfs(string, idx): 
            # 문자열 완성 조건 
            if len(string) == n:
                results.append(string)
                return

            for ch in buttons[int(digits[idx])]:
                dfs(string+ch, idx+1)
                
            
        dfs('', 0)
        return results
                
if __name__ == "__main__":
    cases = [
        (("23",), ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        (("",), []),
        (("2",), ["a","b","c"]),
    ]
    for args, exp in cases:
        got = Solution().letterCombinations(*args)
        got = sorted(got or []) if True else got
        ok = got == sorted(exp)
        print("OK " if ok else "FAIL ", args, got, exp)
