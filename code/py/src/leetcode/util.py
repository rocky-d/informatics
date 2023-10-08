from typing import *

import numpy as np
import pandas as pd


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def list_to_ln(ls: List[int]) -> Optional[ListNode]:
    pre_head = node = ListNode()
    for num in ls:
        node.next = ListNode(val = num, next = None)
        node = node.next
    return pre_head.next


def ln_to_list(node: Optional[ListNode]) -> List[int]:
    ls = []
    while node:
        ls.append(node.val)
        node = node.next
    return ls
