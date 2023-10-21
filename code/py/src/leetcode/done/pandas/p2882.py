from rockyutil.leetcode import *


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = ['email'], keep = 'first', inplace = False, ignore_index = False)
