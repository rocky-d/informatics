class TreeNode(object):
    __slots__ = ['val', 'children']

    def __init__(self, val, children):
        self.val = val
        self.children = children


def main():
    n = int(input())
    if n == 1:
        print(0, 'yes')
        print(1)
        return

    k = 0
    nodes = [TreeNode(val = i, children = []) for i in range(n + 1)]
    for node in range(1, 1 + n):
        father = int(input())
        nodes[father].children.append(nodes[node])
        k = max(k, len(nodes[father].children))
    preorder = []
    print(k, end = ' ')
    ok = True

    def dfs(node):
        tmp = len(node.children)
        if 0 != tmp and k != tmp:
            nonlocal ok
            ok = False
        preorder.append(node.val)
        for child in node.children:
            dfs(child)

    dfs(nodes[0].children[0])
    print('yes' if ok else 'no')
    print(*preorder)


if __name__ == '__main__':
    main()
