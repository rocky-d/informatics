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
                    item1 = heappop(s_counter)
                    char1, count1 = chr(-item1[0]), -item1[1]
                    repeats1 = 1
                    ans += repeats1 * char1
                    last1 = count1 - repeats1
                    if 0 < last1:
                        heappush(s_counter, (-ord(char1), -last1))
                else:
                    break
            repeats = min(repeatLimit, count)
            ans += repeats * char
            last = count - repeats
            if 0 < last:
                heappush(s_counter, (-ord(char), -last))
        return ans
