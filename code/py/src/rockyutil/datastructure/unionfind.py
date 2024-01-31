class UnionFind(object):

    def __init__(self, __heads, *, compressed = True, grouped = False, recursive = False):
        self._heads = __heads
        self._ranks = ... if not compressed else None
        self._groups = {x: [x] for x in self._heads} if grouped else None

    def __len__(self):
        return len(self._heads), len(self._groups)

    def find_cr(self, a):
        if a == self._heads[a]:
            return a
        self._heads[a] = self.find_cr(self._heads[a])
        return self._heads[a]

    def find_ci(self, a):
        a_ = a
        cnt = 0
        while a != self._heads[a]:
            cnt += 1
            a = self._heads[a]
        for _ in range(cnt):
            self._heads[a_] = a
            a_ = self._heads[a_]
        return a

    def union_c(self, a, b):
        a_head, b_head = self.find_c(a), self.find_c(b)
        if a_head != b_head:
            if len(self._groups[a_head]) < len(self._groups[b_head]):
                self._heads[a] = self._heads[a_head] = b_head
                if self._groups is not None:
                    self._groups[b_head] += self._groups.pop(a_head)
            else:
                self._heads[b] = self._heads[b_head] = a_head
                if self._groups is not None:
                    self._groups[a_head] += self._groups.pop(b_head)

    def find_rr(self, a):
        if a == self._heads[a]:
            return a
        return self.find_rr(self._heads[a])

    def find_ri(self, a):
        while a != self._heads[a]:
            a = self._heads[a]
        return a

    def union_r(self, a, b):
        a_head, b_head = self.find_r(a), self.find_r(b)


class UnionFindList(UnionFind):

    def __init__(self, __size, *, compressed = True, grouped = False, recursive = False):
        super().__init__([x for x in range(__size)], compressed = compressed, grouped = grouped, recursive = recursive)


class UnionFindDict(UnionFind):

    def __init__(self, __iterable, *, compressed = True, grouped = False, recursive = False):
        super().__init__({x: x for x in __iterable}, compressed = compressed, grouped = grouped, recursive = recursive)
