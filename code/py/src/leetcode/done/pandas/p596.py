from rockyutil.leetcode import *


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt = courses.groupby('class').size()
    return cnt[cnt > 5].reset_index()[['class']]
