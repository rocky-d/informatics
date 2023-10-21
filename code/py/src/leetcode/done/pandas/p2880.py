from rockyutil.leetcode import *


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[101 == students['student_id'], ['name', 'age']]
