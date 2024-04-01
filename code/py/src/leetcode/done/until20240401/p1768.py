class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        for char1, char2 in zip(word1, word2):
            word += char1 + char2
        return word + (word2[len(word1):] if len(word1) < len(word2) else word1[len(word2):])


eg_word1 = "ab"
eg_word2 = "pqrs"
print(Solution().mergeAlternately(word1 = eg_word1, word2 = eg_word2))
