from rockyutil.leetcode import *


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[views['author_id'] == views['viewer_id'], ['author_id']].drop_duplicates(subset = ['author_id']).sort_values(by = ['author_id']).rename(columns = {'author_id': 'id'})
