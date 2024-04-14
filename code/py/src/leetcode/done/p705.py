class MyHashSet:
    def __init__(self) -> None:
        self.val = False
        self.nxts = {}

    def add(self, key: int) -> None:
        node = self
        for char in str(key):
            if char not in node.nxts.keys():
                node.nxts[char] = MyHashSet()
            node = node.nxts[char]
        node.val = True

    def remove(self, key: int) -> None:
        node = self
        for char in str(key):
            if char not in node.nxts.keys():
                break
            node = node.nxts[char]
        else:
            node.val = False

    def contains(self, key: int) -> bool:
        node = self
        for char in str(key):
            if char not in node.nxts.keys():
                res = False
                break
            node = node.nxts[char]
        else:
            res = node.val
        return res
