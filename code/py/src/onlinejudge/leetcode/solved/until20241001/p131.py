from onlinejudge.leetcode import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = deque()
        n = len(s)

        def dfs(lft: int, rit: int) -> None:
            if rit == n:
                if lft == rit:
                    ans.append(list(partition))
                return
            rit += 1
            dfs(lft, rit)
            palindrome = s[lft:rit]
            if palindrome == palindrome[::-1]:
                partition.append(palindrome)
                dfs(rit, rit)
                partition.pop()

        dfs(lft = 0, rit = 0)
        return ans
