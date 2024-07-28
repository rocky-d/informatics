class SegmentTreeNode(object):
    def __init__(self, lo, hi, val, lft, rit):
        self.lo = lo
        self.hi = hi
        self.val = val
        self.lft = lft
        self.rit = rit


def build(lo, hi):
    if lo == hi:
        return SegmentTreeNode(lo = lo, hi = hi, val = nums[lo], lft = None, rit = None)
    mid = lo + hi >> 1
    lft, rit = build(lo, mid), build(mid + 1, hi)
    return SegmentTreeNode(lo = lo, hi = hi, val = max(lft.val, rit.val), lft = lft, rit = rit)


def query(lo, hi, node):
    if lo == node.lo and hi == node.hi:
        return node.val
    mid = node.lo + node.hi >> 1
    if hi <= mid:
        res = query(lo, hi, node.lft)
    elif mid + 1 <= lo:
        res = query(lo, hi, node.rit)
    else:
        res = max(query(lo, mid, node.lft), query(mid + 1, hi, node.rit))
    return res


if __name__ == '__main__':
    nums = [9, 1, 42, 5, 1, 6, 1, 45, 1, 4, 5, 6, 67, 78, 21, 1, 6, 1, 5]
