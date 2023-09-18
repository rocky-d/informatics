# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head.next
        old_head = head
        while head is not None and old_head.next is not None:
            # print(head.val)
            old_head = head
            old_next = head.next
            head.next = old_head.next.next.next
            old_next.next = head
            head = head.next
            # output(head)
        output(head)
        return res
# 3, 4, None

def output(head):
    while head is not None:
        print(head.val, end = ' > ')
        head = head.next
    print('')


ls = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
output(Solution.swapPairs(None, ls))
