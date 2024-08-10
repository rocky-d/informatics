from math import ceil


def main() -> None:
    n, l, r = map(int, input().split())
    h = map(int, input().split())

    total = sum(h)
    guests = n - l
    diff = r - l
    times = ceil(guests / diff)
    least = guests + l * (2 * times - 1)
    print('No' if total < least else 'Yes')


if __name__ == '__main__':
    main()
