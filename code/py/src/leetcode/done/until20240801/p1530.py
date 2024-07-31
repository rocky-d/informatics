from rockyutil.leetcode import *


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> List[int]:
            nonlocal ans
            if node is None:
                return []
            lfts, rits = dfs(node.left), dfs(node.right)
            ans += sum(1 for lft in lfts for rit in rits if lft + rit <= distance)
            return [1] if 0 == len(lfts) == len(rits) else [val + 1 for val in chain(lfts, rits)]

        dfs(node = root)
        return ans
