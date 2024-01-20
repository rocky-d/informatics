from rockyutil.leetcode import *


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return reduce(list.__add__, [[w for w in word.split(separator) if 0 < len(w)] for word in words])


eg_words = ['$easy$', '$no$problem$']
eg_separator = '$'
print(Solution().splitWordsBySeparator(words = eg_words, separator = eg_separator))
