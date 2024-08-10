from functools import reduce


def main():
    a, b = map(int, input().split())

    ans = []
    maxm = 0
    for num1 in range(a, b + 1):
        num = str(num1)
        steps = 0
        lst, num = num, str(reduce(lambda x, y: x * y, map(int, num), 1))
        while lst != num:
            lst, num = num, str(reduce(lambda x, y: x * y, map(int, num), 1))
            steps += 1
        if steps > maxm:
            maxm = steps
            ans.clear()
            ans.append(num1)
        elif steps == maxm:
            ans.append(num1)
    print(maxm)
    print(*ans)


if __name__ == '__main__':
    main()
