from onlinejudge.leetcode import *


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = ''
        heap = [(-ord(char), -count) for char, count in Counter(s).items()]
        heapify(heap)
        while 0 < len(heap):
            item = heappop(heap)
            char, cnt = chr(-item[0]), -item[1]
            if 0 < len(ans) and ans[-1] == char:
                if 0 < len(heap):
                    item_ = heappop(heap)
                    char_, cnt_ = chr(-item_[0]), -item_[1]
                    repeats_ = 1
                    ans += repeats_ * char_
                    lst_ = cnt_ - repeats_
                    if 0 < lst_:
                        heappush(heap, (-ord(char_), -lst_))
                else:
                    break
            repeats = min(repeatLimit, cnt)
            ans += repeats * char
            lst = cnt - repeats
            if 0 < lst:
                heappush(heap, (-ord(char), -lst))
        return ans
