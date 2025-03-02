from onlinejudge.leetcode import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = lft = rit = ListNode(next=head)
        for _ in range(1 + n):
            rit = rit.next
        while rit is not None:
            lft, rit = lft.next, rit.next
        lft.next = lft.next.next
        return dummy.next


eg_head = link([1, 2, 3, 4, 5])
eg_n = 2
print(*unlink(Solution().removeNthFromEnd(eg_head, eg_n)))
