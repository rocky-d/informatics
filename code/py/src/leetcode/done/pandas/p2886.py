from rockyutil.leetcode import *


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int})
