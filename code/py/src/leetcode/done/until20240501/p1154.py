from rockyutil.leetcode import *


class Solution:
    def dayOfYear(self, date: str) -> int:
        return int((datetime.datetime.strptime(date, '%Y-%m-%d')).strftime('%j'))
