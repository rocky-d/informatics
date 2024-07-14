from rockyutil.leetcode import *


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = frozenset(nums)
        dummy = node = ListNode(next = head)
        while node.next is not None:
            if node.next.val in nums:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
