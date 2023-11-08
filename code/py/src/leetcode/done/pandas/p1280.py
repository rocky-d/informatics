from rockyutil.leetcode import *


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(students, subjects, how = 'cross').sort_values(['student_id', 'subject_name']).merge(examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams'), on = ['student_id', 'subject_name'], how = 'left').fillna(0)[['student_id', 'student_name', 'subject_name', 'attended_exams']]
