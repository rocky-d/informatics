from rockyutil.leetcode import *


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        letter_counter = Counter()
        for word in words:
            letter_counter += Counter(word)
        for letter, count in letter_counter.items():
            if 0 != count % n:
                ans = False
                break
        else:
            ans = True
        return ans


eg_words = ['abc', 'aabc', 'bc']
print(Solution().makeEqual(words = eg_words))
