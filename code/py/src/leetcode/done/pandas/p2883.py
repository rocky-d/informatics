from rockyutil.leetcode import *


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = 'name')
