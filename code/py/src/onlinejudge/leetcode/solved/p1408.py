from onlinejudge.leetcode import *


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        words.sort(key=len)
        for i in range(n):
            words_i = words[i]
            for j in range(i + 1, n):
                if words_i in words[j]:
                    ans.append(words_i)
                    break
        return ans


eg_words = ['leetcoder', 'leetcode', 'od', 'hamlet', 'am']
print(Solution().stringMatching(eg_words))
