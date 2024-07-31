class _UnionFind(object):

    def __init__(self, __heads, *, generic, grouped = False, recursive = False, compressed = True):
        self._heads = __heads
        self._generic = generic
        if grouped:
            # self._groups = {x: 1 for x in self._heads}
            self._groups = {x: [x] for x in self._heads}
        else:
            self._groups = None
        if recursive:
            self._find_comp = self._find_comp_recu
            self._find_rank = self._find_rank_recu
        else:  # iterative
            self._find_comp = self._find_comp_iter
            self._find_rank = self._find_rank_iter
        if compressed:
            self._ranks = None
            self.find = self._find_comp
            self.union = self._union_comp
        else:  # ranked
            if self._generic:
                self._ranks = {x: 0 for x in self._heads}
            else:
                self._ranks = [0 for _ in self._heads]
            self.find = self._find_rank
            self.union = self._union_rank

    # def __len__(self):  # TODO
    #     return len(self._heads), len(self._groups) if self._groups is not None else None

    def _find_comp_recu(self, x):
        if x == self._heads[x]:
            return x
        self._heads[x] = self._find_comp_recu(self._heads[x])
        return self._heads[x]

    def _find_comp_iter(self, x):
        x_ = x
        cnt = 0
        while x != self._heads[x]:
            cnt += 1
            x = self._heads[x]
        for _ in range(cnt):
            self._heads[x_] = x
            x_ = self._heads[x_]
        return x

    def _union_comp(self, u, v):
        u_head, v_head = self._find_comp(u), self._find_comp(v)
        if u_head != v_head:
            if self._groups is None:
                self._heads[u] = self._heads[u_head] = v_head
            else:
                if len(self._groups[u_head]) < len(self._groups[v_head]):
                    self._heads[u] = self._heads[u_head] = v_head
                    self._groups[v_head] += self._groups.pop(u_head)
                else:
                    self._heads[v] = self._heads[v_head] = u_head
                    self._groups[u_head] += self._groups.pop(v_head)

    def _find_rank_recu(self, x):
        if x == self._heads[x]:
            return x
        return self._find_rank_recu(self._heads[x])

    def _find_rank_iter(self, x):
        while x != self._heads[x]:
            x = self._heads[x]
        return x

    def _union_rank(self, u, v):
        u_head, v_head = self._find_rank(u), self._find_rank(v)
        if u_head != v_head:
            if self._ranks[u_head] < self._ranks[v_head]:
                self._heads[u_head] = v_head
                if self._groups is not None:
                    self._groups[v_head] += self._groups.pop(u_head)
            else:
                self._heads[v_head] = u_head
                if self._groups is not None:
                    self._groups[u_head] += self._groups.pop(v_head)
                if self._ranks[u_head] == self._ranks[v_head]:
                    self._ranks[u_head] += 1
                    if self._generic:
                        self._ranks.pop(v_head)


class UnionFindList(_UnionFind):  # TODO: set properties

    def __init__(self, __size, *, grouped = False, recursive = False, compressed = True):
        super().__init__(
            list(range(__size)), generic = False,
            grouped = grouped, recursive = recursive, compressed = compressed
        )


class UnionFindDict(_UnionFind):  # TODO: set properties

    def __init__(self, __iterable, *, grouped = False, recursive = False, compressed = True):
        super().__init__(
            {x: x for x in __iterable}, generic = True,
            grouped = grouped, recursive = recursive, compressed = compressed
        )


if __name__ == '__main__':
    import random

    ufl = UnionFindList(100, grouped = True, recursive = True, compressed = False)
    ufd = UnionFindDict((-i for i in range(100)), grouped = True, recursive = True, compressed = False)

    for _ in range(50):
        x, y = random.randint(a = 0, b = 99), random.randint(a = 0, b = 99)
        ufl.union(x, y)
        ufd.union(-x, -y)
    print(ufl._groups)
    print(ufd._groups)
