from rockyutil.leetcode import *


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        decreasing_stack = [ListNode(val = 100_000, next = head)]
        node = head
        while node is not None:
            while node.next is not None and node.val < node.next.val:
                parent = decreasing_stack.pop(-1)
                parent.next = node.next
                node = parent
            decreasing_stack.append(node)
            node = node.next
        return decreasing_stack[1]


eg_head = ListNode.list_to_ln(ls = [5, 2, 13, 3, 8])
print(ListNode.ln_to_list(head = Solution().removeNodes(head = eg_head)))
