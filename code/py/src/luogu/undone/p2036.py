class Solution:
    def __init__(self) -> None:
        self.res = int(1e9)
        self.n = int(input())
        self.sb = [list(map(int, input().split())) for _ in range(self.n)]

    def dfs(self, i: int, s: int, b: int) -> None:
        if i == self.n:
            if not (s == 1 and b == 0):
                self.res = min(self.res, abs(s - b))
        else:
            self.dfs(i + 1, s * self.sb[i][0], b + self.sb[i][1])
            self.dfs(i + 1, s, b)


def main() -> None:
    solution = Solution()
    solution.dfs(0, 1, 0)
    print(solution.res)


if __name__ == '__main__':
    main()
