# import array
import bisect
# import calendar
# import cmath
import collections
import copy
# import csv
import datetime
import functools
# import hashlib
import heapq
import itertools
import json
import math
import operator
import os
# import queue
import random
import re
import string
import sys
import threading
# import time
# import typing
# from array import *
from bisect import *
# from calendar import *
# from cmath import *
from collections import *
from copy import *
# from csv import *
from datetime import *
from functools import *
# from hashlib import *
from heapq import *
from itertools import *
from json import *
from math import *
from operator import *
# from os import *
# from queue import *
from random import *
from re import *
from string import *
from sys import *
# from threading import *
# from time import *
from typing import *

import numpy as np
import pandas as pd
import sortedcontainers as sc


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def link(__iterable):
    dummy = node = ListNode()
    for item in __iterable:
        node.next = ListNode(val = item, next = None)
        node = node.next
    return dummy.next


def unlink(__head):
    node = __head
    while node is not None:
        yield node.val
        node = node.next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a Node.
class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children


if __name__ == '__main__':
    ...
