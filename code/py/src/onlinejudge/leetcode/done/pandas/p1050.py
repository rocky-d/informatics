from onlinejudge.leetcode import *


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return (lambda df: df.loc[3 <= df['cnt'], ['actor_id', 'director_id']])(df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name = 'cnt'))
