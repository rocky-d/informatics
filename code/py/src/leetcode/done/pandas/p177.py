from rockyutil.leetcode import *


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(['salary'], inplace = True)
    return pd.DataFrame({f'getNthHighestSalary({N})': [None]}) if N > len(employee['salary']) else employee.drop('id', axis = 1).sort_values('salary', ascending = False).rename({'salary': f'getNthHighestSalary({N})'}, axis = 1).head(N).tail(1)
