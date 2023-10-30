from rockyutil.leetcode import *


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.sort_values('event_date').drop_duplicates('player_id').rename({'event_date': 'first_login'}, axis = 1)[['player_id', 'first_login']]
