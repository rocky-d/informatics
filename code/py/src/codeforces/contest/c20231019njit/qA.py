def main() -> None:
    n = int(input())
    set_ = set()
    ls = list(map(int, input().split()))
    ans = []
    for num in reversed(ls):
        if num not in set_:
            set_.add(num)
            ans.insert(0, num)
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
