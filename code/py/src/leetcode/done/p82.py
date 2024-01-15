from rockyutil.leetcode import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val = 101, next = head)
        node = dummy
        while node is not None:
            while node.next is not None and node.next.next is not None and node.next.val == node.next.next.val:
                node.next = node.next.next
                while node.next.next is not None and node.next.val == node.next.next.val:
                    node.next = node.next.next
                node.next = node.next.next
            node = node.next
        return dummy.next
