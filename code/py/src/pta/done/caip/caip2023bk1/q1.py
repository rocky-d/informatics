def main() -> None:
    n = int(input())
    nums = [[0, 0, 0, 0], [0, 0, 0, 1]]
    for _ in range(n):
        c, p = map(int, input().split())
        nums[c][p - 1] += 1
    print(*nums[0][:-1])
    print(*nums[1][:-1])
    nums.sort(reverse = True)
    print(('The first win!', 'The second win!')[nums[0][-1]])


if __name__ == '__main__':
    main()
