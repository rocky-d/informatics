from rockyutil.leetcode import *


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (lambda series: series[5 < series].reset_index()[['class']])(courses.groupby('class').size())
