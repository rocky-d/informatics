from rockyutil.leetcode import *


class Solution:
    max_value = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def go_through(node: TreeNode) -> int:
            if node is None:
                return 0
            go_through(node.right)
            node.val += self.max_value
            self.max_value = node.val
            go_through(node.left)
            return node.val

        go_through(root)
        return root
