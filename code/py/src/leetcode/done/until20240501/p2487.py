from rockyutil.leetcode import *


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk_dec = deque([ListNode(val = 100_000, next = head)])
        node = head
        while node is not None:
            while node.next is not None and node.val < node.next.val:
                pre = stk_dec.pop()
                pre.next = node.next
                node = pre
            stk_dec.append(node)
            node = node.next
        return stk_dec[1]


eg_head = link([5, 2, 13, 3, 8])
print(*unlink(Solution().removeNodes(eg_head)))
