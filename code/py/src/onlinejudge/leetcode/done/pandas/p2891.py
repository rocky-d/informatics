from onlinejudge.leetcode import *


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[100 < animals['weight']].sort_values('weight', ascending = False)[['name']]
