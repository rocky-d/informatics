from rockyutil.leetcode import *


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt = courses.groupby('class').size()
    return cnt[5 < cnt].reset_index()[['class']]
