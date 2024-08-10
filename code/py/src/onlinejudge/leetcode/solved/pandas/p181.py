from onlinejudge.leetcode import *


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_with_manager = employee.merge(employee, left_on = 'managerId', right_on = 'id', suffixes = ('_emp', '_mgr'))
    return employee_with_manager[employee_with_manager['salary_emp'] > employee_with_manager['salary_mgr']][['name_emp']].rename(columns = {'name_emp': 'Employee'})
