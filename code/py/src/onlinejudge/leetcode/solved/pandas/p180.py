from onlinejudge.leetcode import *


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['var'] = logs.num.rolling(3).var()
    return pd.DataFrame({'ConsecutiveNums': logs[0 == logs['var']].num.unique()})
