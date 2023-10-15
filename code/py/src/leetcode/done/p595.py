from leetcode.util import *


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[['name', 'population', 'area']].query('3000000 <= area or 25000000 <= population')
