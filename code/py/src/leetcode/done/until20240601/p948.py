from rockyutil.leetcode import *


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans, buffer = 0, 0
        tokens.sort()
        lft, rit = 0, len(tokens) - 1
        while lft <= rit:
            if tokens[lft] <= power:
                power -= tokens[lft]
                ans += 1
                buffer = 0
                lft += 1
            elif 1 <= ans:
                ans -= 1
                buffer += 1
                power += tokens[rit]
                rit -= 1
            else:
                break
        return ans + buffer
