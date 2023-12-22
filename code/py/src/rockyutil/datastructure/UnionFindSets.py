class UnionFindSets(object):

    def __init__(self, size: int) -> None:
        self.parent: list[int] = [i for i in range(size)]
        self.rank: list[int] = [0 for _ in range(size)]

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:  # elif self.rank[root_x] == self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
