class UnionFindSet(object):

    def __init__(self, __supports_getitem):
        self.heads = __supports_getitem

    def find1(self, a):
        if a == self.heads[a]:
            return a
        return self.find1(self.heads[a])

    def find2(self, a):
        if a == self.heads[a]:
            return a
        self.heads[a] = self.find2(self.heads[a])
        return self.heads[a]

    def find3(self, a):
        while a != self.heads[a]:
            a = self.heads[a]
        return a

    def find4(self, a):
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

    find = find4

    def union(self, a, b):
        self.heads[a] = self.heads[self.find(a)] = self.find(b)
