from onlinejudge.leetcode import *


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return (lambda df: df[2 != df['referee_id']][['name']])(customer.fillna(-1))
