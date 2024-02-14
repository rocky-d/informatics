from collections import deque


class UnionFindList(object):
    def __init__(self, __size: int) -> None:
        self._heads = [x for x in range(__size)]
        self._groups = {x: 1 for x in self._heads}

    def find(self, a) -> int:
        a_ = a
        cnt = 0
        while a != self._heads[a]:
            cnt += 1
            a = self._heads[a]
        for _ in range(cnt):
            self._heads[a_] = a
            a_ = self._heads[a_]
        return a

    def union(self, a, b) -> None:
        a_head, b_head = self.find(a), self.find(b)
        if a_head != b_head:
            if self._groups[a_head] < self._groups[b_head]:
                self._heads[a] = self._heads[a_head] = b_head
                self._groups[b_head] += self._groups.pop(a_head)
            else:
                self._heads[b] = self._heads[b_head] = a_head
                self._groups[a_head] += self._groups.pop(b_head)


def main() -> None:
    n, m = map(int, input().split())
    z, x, y = deque(), deque(), deque()
    for _ in range(m):
        zi, xi, yi = input().split()
        z.append(zi), x.append(int(xi)), y.append(int(yi))

    ans = deque()
    ufl = UnionFindList(n + 1)
    for zi, xi, yi in zip(z, x, y):
        if '1' == zi:
            ufl.union(xi, yi)
        else:  # elif '2' == zi:
            ans.append('Y' if ufl.find(xi) == ufl.find(yi) else 'N')
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
