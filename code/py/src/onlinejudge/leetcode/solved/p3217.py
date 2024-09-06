from onlinejudge.leetcode import *


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(next=head)
        nums = frozenset(nums)
        while node.next is not None:
            if node.next.val in nums:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
