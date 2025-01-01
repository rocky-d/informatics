class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        ans = 1
        w = word[k:]
        while not word.startswith(w):
            ans += 1
            w = w[k:]
        return ans


eg_word = 'abcbabcd'
eg_k = 2
print(Solution().minimumTimeToInitialState(eg_word, eg_k))
