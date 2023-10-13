from leetcode.util import *


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    ans_ls = []
    for i in range(employee.shape[0]):
        manager_id = employee.iloc[i, 3]
        if not pd.isnull(manager_id):
            tmp_df = employee.loc[employee['id'] == manager_id]
            if 0 < tmp_df.shape[0] and employee.iloc[i, 2] > tmp_df.iloc[0, 2]:
                ans_ls.append(employee.iloc[i, 1])
    return pd.DataFrame({'Employee': ans_ls})
