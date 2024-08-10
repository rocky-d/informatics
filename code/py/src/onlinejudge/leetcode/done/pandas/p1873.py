from onlinejudge.leetcode import *


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'employee_id': employees['employee_id'], 'bonus': employees.apply(lambda x: 0 if 0 == x['employee_id'] % 2 or 'M' == x['name'][0] else x['salary'], axis = 1)}).sort_values('employee_id')
