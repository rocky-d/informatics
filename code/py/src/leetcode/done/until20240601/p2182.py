from rockyutil.leetcode import *


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = ''
        s_counter = list((-ord(char), -count) for char, count in Counter(s).items())
        heapify(s_counter)
        while 0 < len(s_counter):
            item = heappop(s_counter)
            char, count = chr(-item[0]), -item[1]
            if 0 < len(ans) and ans[-1] == char:
                if 0 < len(s_counter):
                    item_ = heappop(s_counter)
                    char_, count_ = chr(-item_[0]), -item_[1]
                    repeats_ = 1
                    ans += repeats_ * char_
                    last_ = count_ - repeats_
                    if 0 < last_:
                        heappush(s_counter, (-ord(char_), -last_))
                else:
                    break
            repeats = min(repeatLimit, count)
            ans += repeats * char
            last = count - repeats
            if 0 < last:
                heappush(s_counter, (-ord(char), -last))
        return ans
