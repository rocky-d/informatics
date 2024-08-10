class UnionFindList(object):
    def __init__(self, __size: int) -> None:
        self.heads = [x for x in range(__size)]
        self.groups = {x: 1 for x in self.heads}

    def find(self, a: int) -> int:
        a_ = a
        cnt = 0
        while a != self.heads[a]:
            cnt += 1
            a = self.heads[a]
        for _ in range(cnt):
            self.heads[a_] = a
            a_ = self.heads[a_]
        return a

    def union(self, a: int, b: int) -> None:
        a_head, b_head = self.find(a), self.find(b)
        if a_head != b_head:
            if self.groups[a_head] < self.groups[b_head]:
                self.heads[a] = self.heads[a_head] = b_head
                self.groups[b_head] += self.groups.pop(a_head)
            else:
                self.heads[b] = self.heads[b_head] = a_head
                self.groups[a_head] += self.groups.pop(b_head)


def main() -> None:
    n, m = map(int, input().split())
    ufl = UnionFindList(1 + n)
    for _ in range(m):
        ufl.union(*map(int, input().split()))

    print(len(ufl.groups) - 1)
    print(max(ufl.groups.values()))


if __name__ == '__main__':
    main()
