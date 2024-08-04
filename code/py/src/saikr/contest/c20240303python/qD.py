from collections import deque
from math import gcd


def main() -> None:
    n, q = map(int, input().split())
    nums = [(0, 0)]
    for _ in range(n):
        nums.append(tuple(map(int, input().split())))
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))

    ans = deque(maxlen = q)
    gcds = {}
    for i, j in queries:
        lower = nums[i][1] * nums[j][1]
        upper = nums[i][0] * nums[j][1] + nums[j][0] * nums[i][1]
        if (lower, upper) not in gcds:
            gcds[lower, upper] = gcd(lower, upper)
        gcd_ = gcds[lower, upper]
        ans.append(str(upper // gcd_) + '/' + str(lower // gcd_))
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
