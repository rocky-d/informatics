from onlinejudge.leetcode import *


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars = ['product_id'], value_vars = ['store1', 'store2', 'store3'], var_name = 'store', value_name = 'price').dropna(ignore_index = True)
