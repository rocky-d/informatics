from rockyutil.leetcode import *


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        node = head
        while node is not None:
            node = node.next
            cnt += 1
        node = head
        for _ in range(cnt // 2):
            node = node.next
        return node
