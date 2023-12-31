from rockyutil.leetcode import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # res = dummy = ListNode(next = head)
        # while dummy.next and dummy.next.next:
        #     node1 = dummy.next
        #     node2 = node1.next
        #     dummy.next = node2
        #     node1.next = node2.next
        #     node2.next = node1
        #     dummy = node1
        # return res.next

        res = dummy = ListNode(next = head)
        while dummy.next and dummy.next.next:
            node0 = dummy.next
            node1 = node0.next
            node0.next = node1.next
            node1.next = node0
            dummy.next = node1
            dummy = node0
        return res.next


sol = Solution()

ls = [1, 2, 3, 4, 5]
print(ListNode.ln_to_list(sol.swapPairs(ListNode.list_to_ln(ls))))
