class UnionFindList(object):

    def __init__(self, __size, *, grouped = False):
        self._heads = [x for x in range(__size)]
        self._groups = {x: [x] for x in self._heads} if grouped else None

    def __len__(self):
        return len(self._heads), len(self._groups)

    def find1(self, a):
        a_old = a
        cnt = 0
        while a != self._heads[a]:
            cnt += 1
            a = self._heads[a]
        a, head = a_old, a
        for _ in range(cnt):
            self._heads[a] = head
            a = self._heads[a]
        return head

    def find2(self, a):
        if a == self._heads[a]:
            return a
        self._heads[a] = self.find2(self._heads[a])
        return self._heads[a]

    def union(self, a, b):
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

    def find3(self, a):
        while a != self._heads[a]:
            a = self._heads[a]
        return a

    def find4(self, a):
        if a == self._heads[a]:
            return a
        return self.find4(self._heads[a])


class UnionFindDict(object):

    def __init__(self, __iterable, *, grouped = False):
        self._heads = {x: x for x in __iterable}
        self._groups = {x: [x] for x in self._heads} if grouped else None

    def __len__(self):
        return len(self._heads), len(self._groups)
