from rockyutil.leetcode import *


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = deque()
        node = head
        while node is not None:
            stk.append(node.val)
            node = node.next
        node = None
        one = False
        for _ in range(len(stk)):
            val = 2 * stk.pop()
            if one:
                val += 1
            one = 10 <= val
            if one:
                val -= 10
            node = ListNode(val = val, next = node)
        return ListNode(val = 1, next = node) if one else node
