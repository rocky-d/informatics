def main() -> None:
    n = int(input())
    a_list = list(map(int, input().split()))
    a_set = set(a_list)
    sum_a = sum(a_list)
    min_a = min(a_list)
    per = 1
    for i in range(min_a, 1, -1):
        if 0 == sum_a % i:
            for num in a_set:
                if 0 != num % i:
                    break
            else:
                per = i
                break
    print(sum_a // per - n)


if __name__ == '__main__':
    main()
