from leetcode.leetcode import *


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)
    return scores[['score', 'rank']].sort_values('score', ascending = False)
