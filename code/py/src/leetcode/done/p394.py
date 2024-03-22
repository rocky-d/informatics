from rockyutil.leetcode import *


class Solution:
    def decodeString(self, s: str) -> str:
        stk_cnt, stk_str = deque([1]), deque([[]])
        idx, n = 0, len(s)
        while idx < n:
            char = s[idx]
            if char.isdigit():
                cnt = int(char)
                idx += 1
                char = s[idx]
                while char.isdigit():
                    cnt = cnt * 10 + int(char)
                    idx += 1
                    char = s[idx]
                stk_cnt.append(cnt)
            else:
                if '[' == char:
                    stk_str.append([])
                elif ']' == char:
                    stk_str[len(stk_str) - 2].append(stk_cnt.pop() * ''.join(stk_str.pop()))
                else:
                    stk_str[-1].append(char)
                idx += 1
        return stk_cnt.pop() * ''.join(stk_str.pop())


eg_s = '3[a]2[bc]'
print(Solution().decodeString(eg_s))
