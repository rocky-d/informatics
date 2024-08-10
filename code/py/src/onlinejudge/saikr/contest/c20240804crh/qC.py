from math import inf


def main() -> None:
    dct = {}
    city = ''
    people = 0
    while city != 'Moscow':
        cnt, cost, city = input().split()
        cnt, cost = int(cnt), int(cost)
        dct[city] = cnt, cost
        people += cnt

    ans = '', inf
    for start_city in dct.keys():
        start_cnt, start_cost = dct[start_city]
        total = sum(cnt * abs(cost - start_cost) for cnt, cost in dct.values())
        if total < ans[1]:
            ans = start_city, total
    print(*ans)


if __name__ == '__main__':
    main()
