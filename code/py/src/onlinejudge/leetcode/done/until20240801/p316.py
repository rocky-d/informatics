from onlinejudge.leetcode import *


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s_cnter = Counter(s)
        stk_incs, seen = deque([chr(ord('a') - 1)]), set()
        for char in s:
            s_cnter[char] -= 1
            if char not in seen:
                while char < stk_incs[-1] and 0 < s_cnter[stk_incs[-1]]:
                    seen.remove(stk_incs.pop())
                stk_incs.append(char), seen.add(char)
        stk_incs.popleft()
        return ''.join(stk_incs)
