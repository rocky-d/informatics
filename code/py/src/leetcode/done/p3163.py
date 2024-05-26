class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''
        lst, cnt = word[0], 0
        for char in word:
            if lst == char:
                if cnt < 9:
                    cnt += 1
                else:  # elif cnt == 9:
                    ans += '9' + char
                    cnt = 1
            else:
                ans += str(cnt) + lst
                lst, cnt = char, 1
        ans += str(cnt) + lst
        return ans
