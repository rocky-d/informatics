class UnionFindDict(object):
    def __init__(self) -> None:
        self.heads = {}
        self.groups = {}

    def find(self, a: str) -> str:
        if a == self.heads[a]:
            return a
        self.heads[a] = self.find(self.heads[a])
        return self.heads[a]

    def union(self, a: str, b: str) -> None:
        a_head, b_head = self.find(a), self.find(b)
        if a_head != b_head:
            if self.groups[a_head] < self.groups[b_head]:
                self.heads[a] = self.heads[a_head] = b_head
                self.groups[b_head] += self.groups.pop(a_head)
            else:
                self.heads[b] = self.heads[b_head] = a_head
                self.groups[a_head] += self.groups.pop(b_head)


def main() -> None:
    n = int(input())
    ks, ps = [], []
    for _ in range(n):
        k, p = input().split(maxsplit = 1)
        ks.append(int(k))
        ps.append(p.split())
    q = int(input())
    qs = []
    for _ in range(q):
        qs.append(input().split())

    ufd = UnionFindDict()
    for p in ps:
        p0 = p[0]
        if p0 not in ufd.heads:
            ufd.heads[p0] = p0
            ufd.groups[p0] = 1
        for pi in p[1:]:
            if pi not in ufd.heads:
                ufd.heads[pi] = pi
                ufd.groups[pi] = 1
            ufd.union(a = p0, b = pi)
    print(len(ufd.heads), len(ufd.groups))
    for x, y in qs:
        print('Y' if ufd.find(x) == ufd.find(y) else 'N')


if __name__ == '__main__':
    main()
