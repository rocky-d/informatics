from rockyutil.leetcode import *


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        cnter = Counter()
        for word in words:
            for fix, cnt in cnter.items():
                if word.startswith(fix) and word.endswith(fix):
                    ans += cnt
            cnter[word] += 1
        return ans


eg_words = ['a', 'aba', 'ababa', 'aa']
print(Solution().countPrefixSuffixPairs(eg_words))
