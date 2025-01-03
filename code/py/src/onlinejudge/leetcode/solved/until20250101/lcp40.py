from onlinejudge.leetcode import *


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
        odds_lst, odds = odds, []
        for i in range(1, len(odds_lst), 2):
            odds.append(odds_lst[i - 1] + odds_lst[i])
        if 0b1 == 0b1 & cnt:
            if 0 == len(eves):
                return 0
            ans += eves.pop(0)
            cnt -= 1
        i, j = 1, 0
        while 2 <= cnt and j < len(odds) and i < len(eves):
            if eves[i - 1] + eves[i] <= odds[j]:
                ans += odds[j]
                j += 1
            else:
                ans += eves[i - 1] + eves[i]
                i += 2
            cnt -= 2
        i -= 1
        if 0 < cnt:
            if j == len(odds):
                if i + cnt <= len(eves):
                    ans += sum(eves[i:i + cnt])
                    i += cnt
                    cnt -= cnt
                else:
                    ans = 0
            else:
                half = cnt // 2
                if j + half <= len(odds):
                    ans += sum(odds[j:j + half])
                    j += half
                    cnt -= cnt
                else:
                    ans = 0
        return ans


eg_cards = [7, 1, 5, 8, 3, 3, 1, 2]
eg_cnt = 7
print(Solution().maxmiumScore(eg_cards, eg_cnt))
