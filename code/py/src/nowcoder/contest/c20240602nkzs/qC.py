def main():
    n = int(input())

    ans = 0
    nums = set()
    for num in range(1, n + 1):
        total = sum(map(int, str(num)))
        if total % 2 == 0 and (total >= num or total < num and total in nums):
            nums.add(num)
            ans += 1
        else:
            continue
    print(ans)


if __name__ == '__main__':
    main()
