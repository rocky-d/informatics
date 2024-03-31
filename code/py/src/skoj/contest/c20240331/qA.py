def main() -> None:
    s = input()
    k = int(input())

    n = len(s)

    class TrieNode(object):
        def __init__(self, nxts):
            self.nxts = nxts

    root = TrieNode({})

    for i, start in enumerate(s):
        node = root
        for j in range(i, min(n, i + 5)):
            if s[j] not in node.nxts.keys():
                node.nxts[s[j]] = TrieNode({})
            node = node.nxts[s[j]]

    ans = []

    def dfs(node: TrieNode):
        nonlocal k
        if 0 == k:
            return True
        if 0 == len(node.nxts):
            return False
        elif 1 == len(node.nxts):
            char = list(node.nxts.keys())[0]
            k -= 1
            ans.append(char)
            if dfs(node.nxts[char]):
                return True
            ans.pop()
            return False
        else:
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char in node.nxts.keys():
                    k -= 1
                    ans.append(char)
                    if dfs(node.nxts[char]):
                        return True
                    ans.pop()
            return False

    dfs(node = root)
    print(''.join(ans))


if __name__ == '__main__':
    main()
