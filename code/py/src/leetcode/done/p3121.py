class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        idxes = {}
        for i, char in enumerate(word):
            if char.islower() or char not in idxes.keys():
                idxes[char] = i
        for low, upp in zip('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            if -1 != idxes.get(low, -1) and -1 != idxes.get(upp, -1):
                if idxes[low] < idxes[upp]:
                    ans += 1
        return ans
