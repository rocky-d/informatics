from typing import Optional

from leetcode.ln import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = pre_head = ListNode(next = head)
        while pre_head.next and pre_head.next.next:
            node1 = pre_head.next
            node2 = pre_head.next.next
            pre_head.next = node2
            node1.next = node2.next
            node2.next = node1
            pre_head = node1
        return res.next


ls = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
ln_to_list(Solution.swapPairs(..., ls))
