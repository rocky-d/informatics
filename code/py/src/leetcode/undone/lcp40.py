from rockyutil.leetcode import *


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        ans = 0
        cards.sort(reverse = True)
        odds, eves = [], []
        for card in cards:
            ls = odds if 0b1 == 0b1 & card else eves
            ls.append(card)
        if 0b1 == 0b1 & len(odds):
            del odds[-1]
        odds2 = []
        for i in range(1, len(odds), 2):
            odds2.append(odds[i - 1] + odds[i])
        i, j = 1, 0
        while 2 <= cnt and j < len(odds2) and i < len(eves):
            if eves[i - 1] + eves[i] <= odds2[j]:
                ans += odds2[j]
                j += 1
            else:
                ans += eves[i - 1] + eves[i]
                i += 2
            cnt -= 2
        i -= 1
        if 0 < cnt:
            if j == len(odds2):
                if i + cnt <= len(eves):
                    ans += sum(eves[i: i + cnt])
                    i += cnt
                    cnt -= cnt
                else:
                    ans = 0
            elif i == len(eves):
                if 0b0 == 0b1 & cnt and j + cnt // 2 <= len(odds2):
                    ans += sum(odds2[j: j + cnt // 2])
                    j += cnt // 2
                    cnt -= cnt
                else:
                    ans = 0
            elif i + 1 == len(eves):
                if 0b1 == 0b1 & cnt:
                    ans += eves[i]
                    i += 1
                    cnt -= 1
                if 0b0 == 0b1 & cnt and j + cnt // 2 <= len(odds2):
                    ans += sum(odds2[j: j + cnt // 2])
                    j += cnt // 2
                    cnt -= cnt
                else:
                    ans = 0
            else:
                ans += eves[i]
                i += 1
                cnt -= 1
        return ans


eg_cards = [7, 1, 5, 8, 3, 3, 1, 2]
eg_cnt = 7
print(Solution().maxmiumScore(eg_cards, eg_cnt))
