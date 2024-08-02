class SinglyLinkedListNode(object):

    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class DoublyLinkedListNode(object):

    def __init__(self, val, lst, nxt):
        self.val = val
        self.lst = lst
        self.nxt = nxt


class BinaryTreeNode(object):

    def __init__(self, val, lft, rit):
        self.val = val
        self.lft = lft
        self.rit = rit


class SegmentTreeNode(object):

    def __init__(self, lazy, val, lft, rit):
        self.lazy = lazy
        self.val = val
        self.lft = lft
        self.rit = rit


class NaryTreeNode(object):

    def __init__(self, val, nxts):
        self.val = val
        self.nxts = nxts


class TrieNode(object):

    def __init__(self, val, nxts):
        self.val = val
        self.nxts = nxts


if __name__ == '__main__':
    ...
