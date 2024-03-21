from rockyutil.leetcode import *


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(parent: Optional[ListNode], node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return parent
            res = dfs(node, node.next)
            node.next = parent
            return res

        return dfs(parent = None, node = head)
