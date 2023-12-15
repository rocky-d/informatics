from rockyutil.leetcode import *


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []

        def traverse(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return
            if 1 == level % 2:
                index = (level - 1) // 2
                while not index < len(stack):
                    stack.append([])
                stack[index].append(node.val)
            traverse(node = node.left, level = level + 1)
            traverse(node = node.right, level = level + 1)

        def update(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return
            if 1 == level % 2:
                index = (level - 1) // 2
                node.val = stack[index].pop(-1)
            update(node = node.left, level = level + 1)
            update(node = node.right, level = level + 1)

        traverse(root, 0)
        update(root, 0)
        return root
