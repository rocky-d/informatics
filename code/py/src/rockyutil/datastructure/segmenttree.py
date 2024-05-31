class SegmentTreeNode(object):
    def __init__(self, seg, val, lft, rit):
        self.seg = seg
        self.val = val
        self.lft = lft
        self.rit = rit


nums = [9, 1, 42, 5, 1, 6, 1, 45, 1, 4, 5, 6, 67, 78, 21, 1, 6, 1, 5]


def build(l, r):
    if l == r:
        return SegmentTreeNode(seg = (l, r), val = nums[l], lft = None, rit = None)
    mid = l + r >> 1
    lft, rit = build(l, mid), build(mid + 1, r)
    return SegmentTreeNode(seg = (l, r), val = max(lft.val, rit.val), lft = lft, rit = rit)


def query(l, r, node):
    if (l, r) == node.seg:
        return node.val
    mid = node.seg[0] + node.seg[1] >> 1
    if r <= mid:
        res = query(l, r, node.lft)
    elif mid + 1 <= l:
        res = query(l, r, node.rit)
    else:
        res = max(query(l, mid, node.lft), query(mid + 1, r, node.rit))
    return res
