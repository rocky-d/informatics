from rockyutil.leetcode import *


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'],
                         'accounts_count': [(accounts['income'] < 20000).sum(),
                                            ((20000 <= accounts['income']) & (accounts['income'] <= 50000)).sum(),
                                            (50000 < accounts['income']).sum()]})
