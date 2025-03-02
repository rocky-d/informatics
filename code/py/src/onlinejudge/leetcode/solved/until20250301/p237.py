from onlinejudge.leetcode import *


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val, node.next = node.next.val, node.next.next
