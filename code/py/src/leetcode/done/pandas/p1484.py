from rockyutil.leetcode import *


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby('sell_date').agg(num_sold = ('product', 'nunique'), products = ('product', lambda x: ','.join(sorted(set(x))))).reset_index().sort_values('sell_date')
