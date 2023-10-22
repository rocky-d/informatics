from rockyutil.leetcode import *


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$")]
