from onlinejudge.leetcode import *


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(department, employee, how = 'left', left_on = 'id', right_on = 'departmentId')[['name_x', 'name_y', 'salary']].rename(columns = {'name_x': 'Department', 'name_y': 'Employee', 'salary': 'Salary'})
    return df[df.groupby('Department')['Salary'].transform('max') == df['Salary']]
