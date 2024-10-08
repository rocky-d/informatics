from onlinejudge.leetcode import *


class Solution:
    def preorder(self, root: Node) -> List[int]:
        return [] if root is None else reduce(lambda x, y: x + y, (self.preorder(root = child) for child in root.children), [root.val])
