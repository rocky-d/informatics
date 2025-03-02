from onlinejudge.leetcode import *


class FindElements:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.vals = set()

        def dfs(node: Optional[TreeNode], val: int) -> None:
            if node is None:
                return
            self.vals.add(val)
            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)

        dfs(node=root, val=0)

    def find(self, target: int) -> bool:
        return target in self.vals
