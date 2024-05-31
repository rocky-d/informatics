from functools import reduce
from operator import or_


def main() -> None:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        l, r = max(0, n - m), n + m
        if n - m <= 0:
            res = (1 << (n + m).bit_length()) - 1
        else:
            res = reduce(or_, range(l, r, max(1, m >> 1)))
        print(res)


def correct() -> None:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        l, r = max(0, n - m), n + m
        res = 0
        flag = True
        for i in range(31, -1, -1):
            p = 1 << i
            if flag:
                if l & p == r & p:
                    res |= l & p
                else:
                    flag = False
                    res |= p
            else:
                res |= p
        print(res)


if __name__ == '__main__':
    correct()
