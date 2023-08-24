def main():
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    n = int(input())
    target = input().split()
    for _ in range(n):
        i = 7
        nums = set(input().split())
        for num in nums:
            if num in target:
                i -= 1
        res[i] += 1
    del res[-1]
    print(*res)


if __name__ == '__main__':
    main()
