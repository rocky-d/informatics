class Trie:
    def __init__(self) -> None:
        self.val = 0
        self.nxts = {}

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.nxts.keys():
                node.nxts[char] = Trie()
            node = node.nxts[char]
        node.val += 1

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.nxts.keys():
                res = False
                break
            node = node.nxts[char]
        else:
            res = 0 < node.val
        return res

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.nxts.keys():
                res = False
                break
            node = node.nxts[char]
        else:
            res = True
        return res
