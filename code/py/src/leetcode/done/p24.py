from typing import Optional

from leetcode.ln import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode(next = head)
        while dummy.next and dummy.next.next:
            node1 = dummy.next
            node2 = node1.next
            dummy.next = node2
            node1.next = node2.next
            node2.next = node1
            dummy = node1
        return res.next


sol = Solution()
ls = [1, 2, 3, 4, 5]
print(ln_to_list(sol.swapPairs(list_to_ln(ls))))
