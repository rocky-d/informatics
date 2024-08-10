from onlinejudge.leetcode import *


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next is not None:
            node.next = ListNode(val = gcd(node.val, node.next.val), next = node.next)
            node = node.next.next
        return head
