class UnionFindSet(object):
    def __init__(self, __heads: dict[tuple[int, int, int], tuple[int, int, int]]) -> None:
        self.heads = __heads
        self.groups = {head: 1 for head in self.heads}

    def find(self, a):
        if a == self.heads[a]:
            return a
        self.heads[a] = self.find(self.heads[a])
        return self.heads[a]

    def union(self, a: tuple[int, int, int], b: tuple[int, int, int]) -> None:
        a_head, b_head = self.find(a), self.find(b)
        if a_head != b_head:
            self.heads[a] = self.heads[a_head] = b_head
            self.groups[b_head] += self.groups.pop(a_head)


def main() -> None:
    m, n, l, t = map(int, input().split())
    slices = []
    for _ in range(l):
        slices.append([])
        for _ in range(m):
            slices[-1].append(input().split())

    ufs = UnionFindSet({})
    for i in range(l):
        for j in range(m):
            for k in range(n):
                if '1' == slices[i][j][k]:
                    ufs.heads[i, j, k] = i, j, k
                    ufs.groups[i, j, k] = 1
                    if 0 <= i - 1 and '1' == slices[i - 1][j][k]:
                        ufs.union((i, j, k), (i - 1, j, k))
                    if 0 <= j - 1 and '1' == slices[i][j - 1][k]:
                        ufs.union((i, j, k), (i, j - 1, k))
                    if 0 <= k - 1 and '1' == slices[i][j][k - 1]:
                        ufs.union((i, j, k), (i, j, k - 1))
    print(sum(vol for vol in ufs.groups.values() if t <= vol))


if __name__ == '__main__':
    main()
