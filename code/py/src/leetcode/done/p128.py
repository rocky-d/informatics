from rockyutil.leetcode import *


class UnionFindList(object):
    def __init__(self, __size, *, grouped = False):
        self._heads = [x for x in range(__size)]
        self._groups = {x: [x] for x in self._heads} if grouped else None

    def __len__(self):
        return len(self._heads), len(self._groups)

    def find1(self, a):
        a_ = a
        cnt = 0
        while a != self._heads[a]:
            cnt += 1
            a = self._heads[a]
        for _ in range(cnt):
            self._heads[a_] = a
            a_ = self._heads[a_]
        return a

    def union1(self, a, b):
        a_head, b_head = self.find1(a), self.find1(b)
        if a_head != b_head:
            if len(self._groups[a_head]) < len(self._groups[b_head]):
                self._heads[a] = self._heads[a_head] = b_head
                if self._groups is not None:
                    self._groups[b_head] += self._groups.pop(a_head)
            else:
                self._heads[b] = self._heads[b_head] = a_head
                if self._groups is not None:
                    self._groups[a_head] += self._groups.pop(b_head)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0
        nums = frozenset(nums)
        ufs = UnionFindList(len(nums), grouped = True)
        seen = dict()
        for i, num in enumerate(nums):
            if num - 1 in seen.keys():
                ufs.union1(i, seen[num - 1])
            if num + 1 in seen.keys():
                ufs.union1(i, seen[num + 1])
            seen[num] = i
        return len(max(ufs._groups.values(), key = lambda value: len(value)))
