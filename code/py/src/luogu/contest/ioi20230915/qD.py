def main() -> None:
    n, m = map(int, input().split())
    c_score = [None] + list(map(int, input().split()))
    res = 0
    for i in list(map(int, input().split())):
        if i <= n and c_score[i] < 200:
            res += 1
    print(res)


if __name__ == '__main__':
    main()
