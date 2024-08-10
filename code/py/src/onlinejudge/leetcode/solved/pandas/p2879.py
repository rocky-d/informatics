from onlinejudge.leetcode import *


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
