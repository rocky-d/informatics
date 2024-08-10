from onlinejudge.leetcode import *


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [word for word in separator.join(words).split(separator) if 0 < len(word)]


eg_words = ['$easy$', '$no$problem$']
eg_separator = '$'
print(Solution().splitWordsBySeparator(words = eg_words, separator = eg_separator))
