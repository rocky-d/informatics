class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        k = 100 - discount
        ord_0, ord_9 = ord('0'), ord('9')
        words = sentence.split(' ')
        for i, word in enumerate(words):
            word1 = word[1:]
            if '$' == word[0] and 0 < len(word1) and all(ord_0 <= ord(char) <= ord_9 for char in word1):
                s = str(k * int(word1)).zfill(3)
                words[i] = '$' + s[:-2] + '.' + s[-2:]
        return ' '.join(words)
