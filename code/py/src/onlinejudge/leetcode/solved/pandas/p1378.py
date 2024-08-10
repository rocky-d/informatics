from onlinejudge.leetcode import *


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, how = 'left', on = 'id')[['unique_id', 'name']]
