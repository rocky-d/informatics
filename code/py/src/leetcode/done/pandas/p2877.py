from rockyutil.leetcode import *


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame({'student_id': [row[0] for row in student_data], 'age': [row[1] for row in student_data]})
