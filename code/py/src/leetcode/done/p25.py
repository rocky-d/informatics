from leetcode.util import *


class Solution:
    @staticmethod
    def is_long_enough_recu(node: Optional[ListNode], length: int) -> bool:
        if length < 1:
            return True
        if node.next:
            return Solution.is_long_enough_recu(node.next, length - 1)
        else:
            return False

    @staticmethod
    def is_long_enough_iter(node: Optional[ListNode], length: int) -> bool:
        for _ in range(length):
            node = node.next
            if not node:
                return False
        return True

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = dummy = ListNode(next = head)
        k1 = k - 1
        while Solution.is_long_enough_iter(dummy, k):
            first = dummy.next
            node0 = dummy
            node1 = node0.next
            node2 = node1.next
            for _ in range(k1):
                node0 = node1
                node1 = node2
                node2 = node2.next
                node1.next = node0
            first.next = node2
            dummy.next = node1
            dummy = first
        return res.next


sol = Solution()

ls = [1, 2, 3, 4, 5, 6, 7]
print(ln_to_list(sol.reverseKGroup(list_to_ln(ls), 3)))
