from itertools import groupby


def main() -> None:
    n = int(input())
    s = input()

    ls = []
    infi = False
    for char, group in groupby(s):
        if char == '#':
            continue
        x = len(list(group))
        ls.append(x)
        if 3 <= x:
            infi = True
    if infi:
        ans = 2
    else:
        ans = sum(ls)
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
