from leetcode.leetcode import *


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[['name', 'population', 'area']][(3000000 <= world['area']) | (25000000 <= world['population'])]
