from onlinejudge.leetcode import *


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(next=head)
        nums = frozenset(nums)
        while node is not None and node.next is not None:
            while node.next is not None and node.next.val in nums:
                node.next = node.next.next
            node = node.next
        return dummy.next
