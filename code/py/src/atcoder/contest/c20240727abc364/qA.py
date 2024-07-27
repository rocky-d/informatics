from itertools import pairwise


def main() -> None:
    n = int(input())
    s = (input() for _ in range(n - 1))

    for lst, nxt in pairwise(s):
        if 'sweet' == lst == nxt:
            ans = 'No'
            break
    else:
        ans = 'Yes'
    print(ans)


if __name__ == '__main__':
    main()
