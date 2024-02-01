from rockyutil.nowcoder import *


class Solution:
    def traverse(self, node, new) -> ListNode:
        if node is None:
            return new
        else:
            next = node.next
            node.next = new
            return self.traverse(next, node)

    def ReverseList(self, head: ListNode) -> ListNode:
        return self.traverse(head, None)
