from rockyutil.leetcode import *


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id': pd.Series.nunique, 'partner_id': pd.Series.nunique}).reset_index().rename({'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}, axis = 1)
