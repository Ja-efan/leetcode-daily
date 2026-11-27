"""
LC 207 - Course Schedule
Link: https://leetcode.com/problems/course-schedule/
Difficulty: Medium
Topics: BFS/DFS

Approach:
- 그래프를 선수과목 -> 후속과목 방향으로 저장하고, 과목마다 남은 선수과목 수를 센다. 0인 과목부터 꺼내 들으면서 후속과목의 수를 줄이고, 0이 되면 목록에 넣는다. 들은 과목 수가 전체와 같으면 True.

Time / Space: O(V + E) / O(V + E)

Edge cases:
- 선수과목이 없는 과목(그래프 키에 없는 과목)도 range(numCourses)로 시작 목록에 넣는다
- 사이클(자기 자신 포함)에 속한 과목은 남은 수가 0이 안 돼 끝까지 남는다

Takeaways:
- 선수과목 수가 0인 과목부터 들으며 후속과목의 수를 줄이고, 들은 과목 수를 전체와 비교했다

Revisit? Y
"""
from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 주어진 모든 과목을 수강할 수 있는가 ? 
        # 방향 그래프, 근데 사이클이 없어야 함. 
        # 사이클이 있으면 전체 과목을 수강하지 못함 
        # 주어진 배열을 그래프로 표현 defaultdict(list)
        # k: v = pre_course: courses 
        # 우선 수강해야할 과목이 없는 과목부터 허나씩 지워나간다. -> O(n^2)? 
        
        from collections import defaultdict
        dep = defaultdict(list)
        
        # 수강 완료한 과목 개수 
        # finished = set()
        finished = 0
        
        # 수강 가능 여부 확인 리스트 -> num_prerequisites[i]가 0인 경우에 과목 i 는 수강 가능하다. 
        num_prerequisites = [0 for _ in range(numCourses)]
        
        # dep 그래프: pre_course -> courses 
        for course, pre_course in prerequisites: 
            dep[pre_course].append(course)
            num_prerequisites[course] += 1
            
        courses = [course for course in range(numCourses) if num_prerequisites[course] == 0]
        
        while courses: 
            course = courses.pop()
            # finished.add(course)
            finished += 1
            for next_course in dep[course]:
                num_prerequisites[next_course] -= 1
                if num_prerequisites[next_course] == 0:
                    courses.append(next_course)
        
        # return True if len(finished) == numCourses else False
        return True if finished == numCourses else False
            
                
        
        
        


if __name__ == "__main__":
    cases = [
        ((2, [[1, 0]]), True),
        ((2, [[1, 0], [0, 1]]), False),
    ]
    for args, exp in cases:
        got = Solution().canFinish(*args)
        print("OK " if got == exp else "FAIL", args, got, exp)
