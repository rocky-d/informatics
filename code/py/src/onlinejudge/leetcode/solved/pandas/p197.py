from onlinejudge.leetcode import *


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    return weather[(weather.shift(1)['temperature'] < weather['temperature']) & (weather.shift(1)['recordDate'] + datetime.timedelta(days=1) == weather['recordDate'])][['id']]
