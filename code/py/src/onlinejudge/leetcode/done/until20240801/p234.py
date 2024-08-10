from onlinejudge.leetcode import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = deque()

        def dfs(node: Optional[ListNode]) -> bool:
            if node is None:
                return True
            vals.append(node.val)
            return dfs(node.next) and node.val == vals.popleft()

        return dfs(node = head)
