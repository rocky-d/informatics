from rockyutil.leetcode import *


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = deque()
        for operation in operations:
            if '+' == operation:
                scores.append(scores[-1] + scores[-2])
            elif 'D' == operation:
                scores.append(2 * scores[-1])
            elif 'C' == operation:
                scores.pop()
            else:
                scores.append(int(operation))
        return sum(scores)
