from rockyutil.leetcode import *


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return (lambda df: df[df['customerId'].isna()][['name']].rename(columns = {'name': 'Customers'}))(df = pd.merge(customers, orders, how = 'left', left_on = 'id', right_on = 'customerId'))
