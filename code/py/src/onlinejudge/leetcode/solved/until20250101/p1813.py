class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(' '), sentence2.split(' ')
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        for i, (word1, word2) in enumerate(zip(words1, words2)):
            if word1 != word2:
                p = len(words1) - i
                ans = all(word1 == word2 for word1, word2 in zip(words1[-p:], words2[-p:]))
                break
        else:
            ans = True
        return ans


eg_sentence1 = 'My name is Haley'
eg_sentence2 = 'My Haley'
print(Solution().areSentencesSimilar(eg_sentence1, eg_sentence2))
