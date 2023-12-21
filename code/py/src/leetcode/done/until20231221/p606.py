from rockyutil.leetcode import *


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode]) -> str:
            if node is None:
                res = ''
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                if 0 != len(left) and 0 != len(right):
                    res = f'{node.val}({left})({right})'
                elif 0 != len(left) and 0 == len(right):
                    res = f'{node.val}({left})'
                elif 0 == len(left) and 0 != len(right):
                    res = f'{node.val}()({right})'
                else:  # elif 0 == len(left) and 0 == len(right):
                    res = f'{node.val}'
            return res

        return dfs(root)
