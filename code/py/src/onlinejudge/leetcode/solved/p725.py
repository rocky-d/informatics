from onlinejudge.leetcode import *


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [ListNode() for _ in range(k)]
        nums, idx = [], 0
        while head is not None:
            nums.append(head.val)
            head = head.next
        div, mod = divmod(len(nums), k)
        for i in range(0, mod):
            node = ans[i]
            for _ in range(div + 1):
                node.next = ListNode(val=nums[idx])
                node = node.next
                idx += 1
            ans[i] = ans[i].next
        for i in range(mod, k):
            node = ans[i]
            for _ in range(div):
                node.next = ListNode(val=nums[idx])
                node = node.next
                idx += 1
            ans[i] = ans[i].next
        return ans
