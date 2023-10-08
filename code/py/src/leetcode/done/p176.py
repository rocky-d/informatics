from leetcode.util import *


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(["salary"], inplace = True)
    if len(employee["salary"].unique()) < 2:
        ans = pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        employee.sort_values("salary", ascending = False, inplace = True)
        employee.drop("id", axis = 1, inplace = True)
        employee.rename({"salary": "SecondHighestSalary"}, axis = 1, inplace = True)
        ans = employee.head(2).tail(1)
    return ans
