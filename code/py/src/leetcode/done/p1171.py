from rockyutil.leetcode import *


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val = 0, next = head)
        pref, jump = 0, {}
        node = dummy
        while node is not None:
            pref += node.val
            jump[pref] = node
            node = node.next
        pref = 0
        node = dummy
        while node is not None:
            pref += node.val
            node.next = jump[pref].next
            node = node.next
        return dummy.next


eg_head = link([1, 2, -3, 3, 1])
print(*unlink(Solution().removeZeroSumSublists(eg_head)))
