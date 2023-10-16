from leetcode.util import *


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[['product_id']][('Y' == products['low_fats']) & ('Y' == products['recyclable'])]
