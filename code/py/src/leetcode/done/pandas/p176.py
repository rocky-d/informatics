from leetcode.util import *


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(['salary'], inplace = True)
    if len(employee['salary']) < 2:
        ans = pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        ans = employee.drop('id', axis = 1).sort_values('salary', ascending = False).rename({'salary': 'SecondHighestSalary'}, axis = 1).head(2).tail(1)
    return ans
