from onlinejudge.leetcode import *


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1 = list1
        for _ in range(a - 1):
            node1 = node1.next
        node1.next, node1 = list2, node1.next.next
        for _ in range(a + 1, b + 1):
            node1 = node1.next
        node2 = list2
        while node2.next is not None:
            node2 = node2.next
        node2.next = node1
        return list1
