# import array
import bisect
import collections
import copy
import datetime
import functools
import heapq
import itertools
import math
import random
import sys
import threading
# from array import *
from bisect import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from itertools import *
from math import *
from random import *
from sys import *
from typing import *

import numpy as np
import pandas as pd
import sortedcontainers as sc


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_ln(iterable):
        dummy = node = ListNode()
        for item in iterable:
            node.next = ListNode(val = item, next = None)
            node = node.next
        return dummy.next

    @staticmethod
    def ln_to_list(head):
        res = []
        node = head
        while node is not None:
            res.append(node.val)
            node = node.next
        return res


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    ...
