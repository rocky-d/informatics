from typing import *

crossed = 0


class TreeNode(object):
    def __init__(
            self,
            from_: int,
            to_: int,
            left: Optional['TreeNode'],
            right: Optional['TreeNode']):
        self.from_ = from_
        self.to_ = to_
        self.ranges = [(from_, to_)]
        self.left = left
        self.right = right


def add_range(dummy: TreeNode, l_: int, r_: int) -> None:
    if dummy.left is None:
        dummy.left = TreeNode(from_ = l_, to_ = r_, left = None, right = None)
        return

    global crossed
    parent = dummy
    node = dummy.left
    while True:
        if node.from_ <= l_ <= node.to_ or node.from_ <= r_ <= node.to_:
            crossed += 1
            node.ranges.append((l_, r_))
            node.from_ = min(node.from_, l_)
            node.to_ = max(node.to_, r_)
            break
        else:
            parent = node
            if r_ < node.from_:
                if node.left is None:
                    node.left = TreeNode(from_ = l_, to_ = r_, left = None, right = None)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(from_ = l_, to_ = r_, left = None, right = None)
                    break
                else:
                    node = node.right


def remove_range(dummy: TreeNode, l_: int, r_: int) -> None:
    global crossed
    parent = dummy
    node = dummy.left
    left_branch = True
    while True:
        if node.from_ <= l_ <= r_ <= node.to_:
            node.ranges.remove((l_, r_))
            if 0 == len(node.ranges):
                if node.left is None and node.right is None:
                    if left_branch:
                        parent.left = None
                    else:
                        parent.right = None
                elif node.left is None and node.right is not None:
                    if left_branch:
                        parent.left = node.right
                    else:
                        ...
                elif node.left is not None and node.right is None:
                    ...
                else:
                    ...

            else:
                crossed -= 1
                node.from_ = min((range_[0] for range_ in node.ranges))
                node.to_ = max((range_[1] for range_ in node.ranges))
            break
        else:
            parent = node
            if r_ < node.from_:
                node = node.left
                left_branch = True
            else:
                node = node.right
                left_branch = False


def main() -> None:
    global crossed
    q = int(input())
    dummy = TreeNode(from_ = 0, to_ = 0, left = None, right = None)
    for _ in range(q - 1):
        op, l, r = input().split()
        l, r = map(int, (l, r))
        if '+' == op:
            add_range(dummy = dummy, l_ = l, r_ = r)
        else:
            remove_range(dummy = dummy, l_ = l, r_ = r)

        print("YES" if 0 < crossed else "NO")


if __name__ == '__main__':
    main()
