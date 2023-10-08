from leetcode.util import *


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. 删除所有重复的薪水.
    employee = employee.drop_duplicates(["salary"])

    # 2. 如果少于 2 个不同的薪水，返回 `np.NaN`。
    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})

    # 3. 把表格按 `salary` 降序排序。
    employee = employee.sort_values("salary", ascending = False)

    # 4. 删除 `id` 列。
    employee.drop("id", axis = 1, inplace = True)

    # 5. 重命名 `salary` 列。
    employee.rename({"salary": "SecondHighestSalary"}, axis = 1, inplace = True)

    # 6, 7. 返回第 2 高的薪水
    return employee.head(2).tail(1)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/second-highest-salary/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
