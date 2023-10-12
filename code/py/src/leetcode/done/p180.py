from leetcode.util import *


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if 0 == logs.shape[0]:
        return pd.DataFrame({'ConsecutiveNums': []})

    ans_set = set()
    last_num, times = logs.iloc[0, 1], 1
    for i in range(1, logs.shape[0]):
        curr_num = logs.iloc[i, 1]
        if last_num == curr_num:
            times += 1
            if 2 < times:
                ans_set.add(last_num)
        else:
            last_num = curr_num
            times = 1
    return pd.DataFrame({'ConsecutiveNums': list(ans_set)})
