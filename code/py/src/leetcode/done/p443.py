from rockyutil.leetcode import *


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        chars.append('')
        char_lst, cnt = '', 1
        for char in chars:
            if char_lst == char:
                cnt += 1
            else:
                for char_new in char_lst + ('' if 1 == cnt else str(cnt)):
                    chars[ans] = char_new
                    ans += 1
                char_lst, cnt = char, 1
        return ans
