from rockyutil.leetcode import *


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def prefixes_set(arr: List[int]) -> Set[int]:
            prefixes = set()
            for num in arr:
                while 0 < num:
                    prefixes.add(num)
                    num //= 10
            return prefixes

        prefixes = prefixes_set(arr = arr1) & prefixes_set(arr = arr2)
        return 0 if 0 == len(prefixes) else len(str(max(prefixes)))
