class UnionFindSet(object):

    def __init__(self, __supports_index):
        self._heads = __supports_index

    def find1(self, a):
        if a == self._heads[a]:
            return a
        return self.find1(self._heads[a])

    def find2(self, a):
        if a == self._heads[a]:
            return a
        self._heads[a] = self.find2(self._heads[a])
        return self._heads[a]

    def find3(self, a):
        while a != self._heads[a]:
            a = self._heads[a]
        return a

    def find4(self, a):
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

    find = find4

    def union(self, a, b):
        self._heads[a] = self._heads[self.find(a)] = self.find(b)
