class UnionFind(object):

    def __init__(self, __heads, grouped = False):
        self.heads = __heads
        if grouped:
            if isinstance(self.heads, list):
                self.groups = [1 for _ in range(len(self.heads))]
            elif isinstance(self.heads, dict):
                self.groups = {head: 1 for head in self.heads.keys()}
            else:
                raise TypeError
        else:
            self.groups = None

    def find1(self, a):
        while a != self.heads[a]:
            a = self.heads[a]
        return a

    def find2(self, a):
        a_old = a
        cnt = 0
        while a != self.heads[a]:
            cnt += 1
            a = self.heads[a]
        a, head = a_old, a
        for _ in range(cnt):
            self.heads[a] = head
            a = self.heads[a]
        return head

    def find3(self, a):
        if a == self.heads[a]:
            return a
        return self.find3(self.heads[a])

    def find4(self, a):
        if a == self.heads[a]:
            return a
        self.heads[a] = self.find4(self.heads[a])
        return self.heads[a]

    find = find4

    def union(self, a, b):
        a_head, b_head = self.find(a), self.find(b)
        if a_head != b_head:
            self.heads[a] = self.heads[a_head] = b_head
            if self.groups is not None:
                self.groups[b_head] += self.groups.pop(a_head)
