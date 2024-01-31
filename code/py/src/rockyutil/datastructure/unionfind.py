class UnionFind(object):

    def __init__(self, __heads, generic, *, grouped = False, recursive = False, compressed = True):
        self._heads = __heads
        self._generic = generic
        if grouped:
            self._groups = {x: [x] for x in self._heads}
        else:
            self._groups = None
        if recursive:
            self._find_c = self._find_cr
            self._find_r = self._find_rr
        else:
            self._find_c = self._find_ci
            self._find_r = self._find_ri
        if compressed:
            self._ranks = None
            self.find = self._find_c
            self.union = self._union_c
        else:
            if self._generic:
                self._ranks = {x: 0 for x in self._heads}
            else:
                self._ranks = [0 for _ in self._heads]
            self.find = self._find_r
            self.union = self._union_r

    def __len__(self):
        return len(self._heads), len(self._groups)

    def _find_cr(self, a):
        if a == self._heads[a]:
            return a
        self._heads[a] = self._find_cr(self._heads[a])
        return self._heads[a]

    def _find_ci(self, a):
        a_ = a
        cnt = 0
        while a != self._heads[a]:
            cnt += 1
            a = self._heads[a]
        for _ in range(cnt):
            self._heads[a_] = a
            a_ = self._heads[a_]
        return a

    def _union_c(self, a, b):
        a_head, b_head = self._find_c(a), self._find_c(b)
        if a_head != b_head:
            if len(self._groups[a_head]) < len(self._groups[b_head]):
                self._heads[a] = self._heads[a_head] = b_head
                if self._groups is not None:
                    self._groups[b_head] += self._groups.pop(a_head)
            else:
                self._heads[b] = self._heads[b_head] = a_head
                if self._groups is not None:
                    self._groups[a_head] += self._groups.pop(b_head)

    def _find_rr(self, a):
        if a == self._heads[a]:
            return a
        return self._find_rr(self._heads[a])

    def _find_ri(self, a):
        while a != self._heads[a]:
            a = self._heads[a]
        return a

    def _union_r(self, a, b):
        a_head, b_head = self._find_r(a), self._find_r(b)
        if a_head != b_head:
            if self._ranks[a_head] < self._ranks[b_head]:
                self._heads[a_head] = b_head
                if self._groups is not None:
                    self._groups[b_head] += self._groups.pop(a_head)
            else:
                self._heads[b_head] = a_head
                if self._groups is not None:
                    self._groups[a_head] += self._groups.pop(b_head)
                if self._ranks[a_head] == self._ranks[b_head]:
                    self._ranks[a_head] += 1
                    if self._generic:
                        self._ranks.pop(b_head)


class UnionFindList(UnionFind):

    def __init__(self, __size, *, grouped = False, recursive = False, compressed = True):
        super().__init__([x for x in range(__size)], generic = False,
                         grouped = grouped, recursive = recursive, compressed = compressed)


class UnionFindDict(UnionFind):

    def __init__(self, __iterable, *, grouped = False, recursive = False, compressed = True):
        super().__init__({x: x for x in __iterable}, generic = True,
                         grouped = grouped, recursive = recursive, compressed = compressed)


if __name__ == '__main__':
    import random

    ufl = UnionFindList(1_000, grouped = True, recursive = True, compressed = False)
    ufd = UnionFindDict((-i for i in range(1_000)), grouped = True, recursive = True, compressed = False)

    for _ in range(200):
        x, y = random.randint(a = 0, b = 999), random.randint(a = 0, b = 999)
        ufl.union
