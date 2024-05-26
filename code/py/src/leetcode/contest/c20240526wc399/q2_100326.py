class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''
        cnt, lst = 1, word[0]
        for char in word[1:]:
            if lst == char:
                cnt += 1
                if 10 == cnt:
                    ans += f"{9}{lst}"
                    cnt = 1
            else:
                ans += f"{cnt}{lst}"
                lst = char
                cnt = 1
        ans += f"{cnt}{lst}"
        return ans
