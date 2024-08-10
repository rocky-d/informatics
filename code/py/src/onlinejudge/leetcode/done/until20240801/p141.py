from onlinejudge.leetcode import *


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast is not None:
            fast = fast.next
            if slow is fast:
                ans = True
                break
            if fast is not None:
                slow, fast = slow.next, fast.next
        else:
            ans = False
        return ans
