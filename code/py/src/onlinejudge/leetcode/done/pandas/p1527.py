from onlinejudge.leetcode import *


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1')]
