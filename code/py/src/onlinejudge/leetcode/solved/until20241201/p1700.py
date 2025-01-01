from onlinejudge.leetcode import *


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        while 0 < len(sandwiches):
            for _ in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.popleft(), sandwiches.popleft()
                    break
                else:
                    students.rotate(-1)
            else:
                ans = len(students)
                break
        else:
            ans = 0
        return ans
