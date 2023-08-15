import math


def main():
    n = int(input())
    opened = set()
    for _ in range(n):
        a, t = input().split()
        a = float(a)
        t = int(t)
        for ti in range(1, t + 1):
            num = math.floor(a * ti)
            if num in opened:
                opened.remove(num)
            else:
                opened.add(num)
    print(*opened)


if __name__ == '__main__':
    main()
