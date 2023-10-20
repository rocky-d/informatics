from rockyutil.leetcode import *


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return (lambda df: df[1 < df['count']][['email']])(df = person.groupby('email').size().reset_index(name = 'count'))
