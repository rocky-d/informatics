from rockyutil.leetcode import *


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = Counter(arr)
        return len(arr_counter) == len(set(arr_counter.values()))
