from rockyutil.leetcode import *


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, counter: Counter) -> int:
            if node.left is None and node.right is None:
                counter[node.val] += 1
                odds = 0
                for count in counter.values():
                    if 1 == count % 2:
                        odds += 1
                counter[node.val] -= 1
                return 1 if odds < 2 else 0
            counter[node.val] += 1
            left = 0 if node.left is None else dfs(node = node.left, counter = counter)
            right = 0 if node.right is None else dfs(node = node.right, counter = counter)
            counter[node.val] -= 1
            return left + right

        return dfs(node = root, counter = Counter())
