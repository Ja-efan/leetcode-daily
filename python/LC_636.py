"""
LC 636 - Exclusive Time of Functions

Link: https://leetcode.com/problems/exclusive-time-of-functions

Approach: stack 
- 

Time / Space: O(M) / O(N) (M: 로그의 길이 (len(logs)), N: 함수 개수)
Edge cases: -
- 

Takeaways: 생각보다 단순한 문제인데, end 시점에 call stack top 함수의 time 을 수정해주는 부분을 생각하지 못했다.
- 
Revisit? N
"""

from typing import *

class Solution:

    def parse_log(self, log:str) -> tuple:
        # log message format: {function_id}:{"start" | "end"}:{timestamp}

        function_id, log_type, timestamp = log.split(':')
        return (int(function_id), log_type, int(timestamp))


    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # logs_rev = logs[::-1]

        exec_time = [0 for _ in range(n)]
        call_stack = list()

        for log in logs:
            function_id, log_type, time = self.parse_log(log)

            if log_type == "start":
                # 새로운 id 의 function 이 호출되었다. -> 이전 호출 함수의 동작이 멈춘다. 
                # -> 현재 함수의 start 로 인해 이전 함수의 실행이 멈추었다. 
                # -> 이전 함수의 실행 시간을 추가해준다. 
                if call_stack:
                    prev_function_id, prev_time = call_stack[-1][0], call_stack[-1][1]
                    exec_time[prev_function_id] += (time - prev_time)

                # (function_id, timestamp) 구조로 call stack 에 추가  
                call_stack.append((function_id, time))

            elif log_type == "end":
                # 늦게 호출된 함수가 무조건 먼저 반환된다. 
                # call stack 의 마지막 function call 을 pop 
                pop_function_id, pop_time = call_stack.pop()
                exec_time[pop_function_id] += (time - pop_time + 1)

                if call_stack:
                    call_stack[-1] = (call_stack[-1][0], time+1)



        return exec_time