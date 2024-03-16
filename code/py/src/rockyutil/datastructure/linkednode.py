class SinglyListNode(object):

    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class DoublyListNode(object):

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

    def __init__(self, segment, val, lft, rit):
        self.segment = segment
        self.val = val
        self.lft = lft
        self.rit = rit


class NaryTreeNode(object):

    def __init__(self, val, nxts):
        self.val = val
        self.nxts = nxts


if __name__ == '__main__':
    ...
