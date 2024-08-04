def main():
    ans = []
    n, m = map(int, input().split())
    belongs = [0b0 for _ in range(m + 1)]
    for i in range(n):
        for item in map(int, input().split(maxsplit = 1)[-1].split()):
            belongs[item] |= 0b1 << i
    # print(owns)
    # print(belongs)
    for _ in range(int(input())):
        a, b = map(int, input().split())
        cnt = (belongs[a] & belongs[b]).bit_count()
        ans.append(cnt)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
