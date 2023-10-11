from leetcode.util import *


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    ans = scores.drop('id', axis = 1)

    if 0 == ans.shape[0]:
        ans['rank'] = []
        return ans

    ans = ans.sort_values('score', ascending = False)
    rank_ls = [rank := 1]
    last_score = ans.iloc[0, 0]
    for i in range(1, ans.shape[0]):
        curr_score = ans.iloc[i, 0]
        if last_score != curr_score:
            last_score = curr_score
            rank += 1
        rank_ls.append(rank)
    ans['rank'] = rank_ls
    return ans
