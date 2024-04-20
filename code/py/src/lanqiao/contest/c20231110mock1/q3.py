def getsum(s) -> int:
    res = 0
    for ch in s:
        res += int(ch)
    return res


def main() -> None:
    # days = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # dict_ = {}
    # for i in range(1, 13):
    #     for j in range(1, 1 + days[i]):
    #         num = getsum(str(i) + str(j))
    #         dict_[num] = dict_.get(num, 0) + 1
    # print(dict_)

    sum_ = {2: 4, 3: 10, 4: 18, 5: 23, 6: 25, 7: 29, 8: 30, 9: 34, 10: 36, 11: 36, 12: 32, 13: 23, 14: 19, 15: 15,
            16: 12, 17: 9, 18: 6, 19: 3, 20: 1}
    sum_leap = {2: 4, 3: 10, 4: 18, 5: 23, 6: 25, 7: 29, 8: 30, 9: 34, 10: 36, 11: 36, 12: 32, 13: 24, 14: 19, 15: 15,
                16: 12, 17: 9, 18: 6, 19: 3, 20: 1}

    ans = 0
    for year in range(1900, 10000):
        year_sum = getsum(str(year))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            ans += sum_leap.get(year_sum, 0)
        else:
            ans += sum_.get(year_sum, 0)

    print(ans)


if __name__ == '__main__':
    main()
