from rockyutil.leetcode import *


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return (lambda df: sales_person[~sales_person['sales_id'].isin(df[df['name'] == 'RED']['sales_id'].unique())][['name']])(pd.merge(company, orders, on = 'com_id'))
