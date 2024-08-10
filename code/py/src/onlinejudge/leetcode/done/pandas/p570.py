from onlinejudge.leetcode import *


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    return (lambda series: series[5 <= series].reset_index()[['managerId']].merge(employee, left_on = 'managerId', right_on = 'id')[['name']])(series = employee.dropna().groupby('managerId').size())
