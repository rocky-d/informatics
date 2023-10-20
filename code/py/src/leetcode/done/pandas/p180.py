from rockyutil.leetcode import *


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['var'] = logs.num.rolling(3).var()
    return pd.DataFrame({'ConsecutiveNums': logs.query('var == 0').num.unique()})
