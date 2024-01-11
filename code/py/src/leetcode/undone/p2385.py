from rockyutil.leetcode import *


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjvex = defaultdict(list)
        
        def dfs(rt):
            if rt:
                if rt.left:
                    adjvex[rt.val].append(rt.left.val)
                    adjvex[rt.left.val].append(rt.val)
                if rt.right:
                    adjvex[rt.val].append(rt.right.val)
                    adjvex[rt.right.val].append(rt.val)
                dfs(rt.left)
                dfs(rt.right)
        
        dfs(root)
        
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)
        
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                x = q.popleft()
                for y in adjvex[x]:
                    if y not in visited:
                        visited.add(y)
                        q.append(y)
        
        return step - 1