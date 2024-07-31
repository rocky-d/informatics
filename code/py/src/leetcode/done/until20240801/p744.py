from rockyutil.leetcode import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(range(len(letters)), ord(target), lo = 0, key = lambda mid: ord(letters[mid])) % len(letters)]
