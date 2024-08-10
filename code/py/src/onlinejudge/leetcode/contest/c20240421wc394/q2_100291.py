class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        occors = {}
        for i, char in enumerate(word):
            if char.islower():
                occors[char] = i
            else:
                if char not in occors:
                    occors[char] = i
        for upp in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            low = upp.lower()
            if occors.get(upp, -1) != -1 and occors.get(low, -1) != -1:
                if occors[low] < occors[upp]:
                    ans += 1
        return ans
