from rockyutil.leetcode import *


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def prefixes(arr: List[int]) -> Set[int]:
            res = set()
            for num in arr:
                while 0 < num:
                    res.add(num)
                    num //= 10
            return res

        common_prefixes = prefixes(arr = arr1) & prefixes(arr = arr2)
        return 0 if 0 == len(common_prefixes) else len(str(max(common_prefixes)))
