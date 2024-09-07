from onlinejudge.leetcode import *


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        n = len(nums)

        def dfs(idx: int, node: Optional[TreeNode]) -> bool:
            if idx == n:
                return True
            if node is None or node.val != nums[idx]:
                return False
            idx += 1
            return dfs(idx, node.left) or dfs(idx, node.right)

        que = deque([root])
        while 0 < len(que):
            node = que.popleft()
            if dfs(idx=0, node=node):
                ans = True
                break
            if node is not None:
                que.append(node.left)
                que.append(node.right)
        else:
            ans = False
        return ans
