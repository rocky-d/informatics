class UnionFindSet(object):

    def __init__(self, __heads, groups_enabled = False):
        self.heads = __heads
        self.groups = {head: 1 for head in self.heads} if groups_enabled else None

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

    find = find2

    def union(self, a, b):
        a_head, b_head = self.find(a), self.find(b)
        if a_head != b_head:
            self.heads[a] = self.heads[a_head] = b_head
            if self.groups is not None:
                self.groups[b_head] += self.groups.pop(a_head)
