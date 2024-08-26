from onlinejudge.leetcode import *


class Solution:
    def postorder(self, root: Node) -> List[int]:
        return [] if root is None else reduce(add, (self.postorder(child) for child in root.children), []) + [root.val]
