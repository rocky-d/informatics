from rockyutil.leetcode import *


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number').size().sort_values()[-1:].reset_index()[['customer_number']]
