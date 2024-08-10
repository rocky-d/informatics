from onlinejudge.leetcode import *


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(columns = 'city', index = 'month', values = 'temperature')
