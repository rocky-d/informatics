from onlinejudge.leetcode import *


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[('Y' == products['low_fats']) & ('Y' == products['recyclable']), ['product_id']]
