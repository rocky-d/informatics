from rockyutil.leetcode import *


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (lambda series: series[5 <= series].reset_index()[['class']])(series = courses.groupby('class').size())
