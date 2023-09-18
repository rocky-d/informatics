# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def list_to_ln(ls: list[int]) -> ListNode:
    pre_head = node = ListNode()
    for num in ls:
        node.next = ListNode(val = num, next = None)
        node = node.next
    return pre_head.next


def ln_to_list(node: ListNode) -> list[int]:
    ls = []
    while node:
        ls.append(node.val)
        node = node.next
    return ls
