from rockyutil.leetcode import *


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace = True, ignore_index = True)
    person.drop_duplicates('email', inplace = True, ignore_index = True)
