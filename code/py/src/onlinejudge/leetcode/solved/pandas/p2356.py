from onlinejudge.leetcode import *


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.drop_duplicates(['teacher_id', 'subject_id']).groupby('teacher_id').size().reset_index(name = 'cnt')
