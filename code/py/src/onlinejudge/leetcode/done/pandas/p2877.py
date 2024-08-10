from onlinejudge.leetcode import *


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])
