from rockyutil.leetcode import *


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(['salary'], inplace = True)
    return pd.DataFrame({'SecondHighestSalary': [None]}) if 2 > len(employee['salary']) else employee[['salary']].sort_values('salary', ascending = False).rename({'salary': 'SecondHighestSalary'}, axis = 1).head(2).tail(1)
