class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        oft = ord('a')
        prefs = [0b0]
        for char in word:
            prefs.append(prefs[-1] ^ 0b1 << ord(char) - oft)
        return sum(1 for lft in range(n) for rit in range(lft + 1, n + 1) if (prefs[lft] ^ prefs[rit]).bit_count() <= 1)


eg_word = 'aabb'
print(Solution().wonderfulSubstrings(eg_word))
