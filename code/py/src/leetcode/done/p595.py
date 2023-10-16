from leetcode.util import *


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(3000000 <= world['area']) | (25000000 <= world['population']), ['name', 'population', 'area']]
