from rockyutil.leetcode import *


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'user_id': users['user_id'], 'name': users['name'].apply(lambda x: x.capitalize())}).sort_values('user_id')
