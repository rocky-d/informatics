from rockyutil.leetcode import *


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        node = head.next
        while node is not None:
            val = 0
            while 0 != node.val:
                val += node.val
                node = node.next
            curr.next = ListNode(val = val)
            curr = curr.next
            node = node.next
        return dummy.next
