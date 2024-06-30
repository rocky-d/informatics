from rockyutil.leetcode import *


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans, val = 0, 0
        letters = Counter(letters)
        scores = [sum(score[ord(char) - ord('a')] for char in word) for word in words]

        def dfs(idx: int) -> None:
            nonlocal ans, val
            if idx == len(words):
                ans = max(ans, val)
                return
            dfs(idx + 1)
            word_cnter = Counter(words[idx])
            if all(cnt <= letters[char] for char, cnt in word_cnter.items()):
                for char, cnt in word_cnter.items():
                    letters[char] -= cnt
                val += scores[idx]
                dfs(idx + 1)
                val -= scores[idx]
                for char, cnt in word_cnter.items():
                    letters[char] += cnt

        dfs(idx = 0)
        return ans
