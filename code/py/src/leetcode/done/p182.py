from leetcode.util import *


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby('email').size().reset_index(name = 'count')
    return df[1 < df['count']][['email']]
