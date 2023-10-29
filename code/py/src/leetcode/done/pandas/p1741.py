from rockyutil.leetcode import *


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.rename({'event_day': 'day'}, axis = 1).groupby(['day', 'emp_id'])['total_time'].sum().reset_index()
