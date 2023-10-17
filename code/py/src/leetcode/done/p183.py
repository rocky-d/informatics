from leetcode.util import *


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, how = 'left', left_on = 'id', right_on = 'customerId')
    return df[df['customerId'].isna()][['name']].rename(columns = {'name': 'Customers'})
