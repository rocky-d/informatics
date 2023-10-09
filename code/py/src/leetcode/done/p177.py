from leetcode.util import *


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(['salary'], inplace = True)
    if len(employee['salary']) < N:
        ans = pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        ans = employee.drop('id', axis = 1).sort_values('salary', ascending = False).rename({'salary': f'getNthHighestSalary({N})'}, axis = 1).head(N).tail(1)
    return ans
