from sys import stdout


def main() -> None:
    def check(mid):
        print('?', mid, mid)
        stdout.flush()
        return int(input()) == mid * mid

    lo, hi = 1, 1000
    while 1 < hi - lo:
        mid = hi + lo >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    print('!', hi)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
