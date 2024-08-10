def new_a(a):
    # if len(a) == 0:
    #     return [['']]
    # if len(a) == 1:
    #     return [['1'], ['0']]
    #
    # res = []
    # if a[0] == '1':
    #     if a[-1] == '1':  # 1 - 1
    #         a[-1] = '0'
    #         res.append(a)
    #     else:  # 1 - 0
    #         res += [['1'] + item + ['0'] for item in new_a(a[1:-1])]
    # else:
    #     if a[-1] == '0':  # 0 - 0
    #         a[0] = '1'
    #         res.append(a)
    #     else:  # 0 - 1
    #         # res.append(a)
    #         a[0] = '1'
    #         res.append(a)
    #         a[0] = '0'
    #         a[-1] = '0'
    #         res.append(a)

    res = [a]
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            res.append(a.copy())
            a[i] = '0'
        else:
            a[i] = '0'
            res.append(a.copy())
            a[i] = '1'
    return res


def main() -> None:
    tests = int(input())
    while tests > 0:
        tests -= 1
        input()
        a = list(input().split())

        # a_ls = new_a(a)
        # print(a_ls)
        res = 0
        for i in range(len(a)):
            if a[i] == '0':
                a[i] = '1'

                current_ones = 0
                cnt = 0
                for ai in a:
                    if ai == '1':
                        current_ones += 1
                    else:
                        cnt += current_ones
                res = max(res, cnt)

                a[i] = '0'
            else:
                a[i] = '0'

                current_ones = 0
                cnt = 0
                for ai in a:
                    if ai == '1':
                        current_ones += 1
                    else:
                        cnt += current_ones
                res = max(res, cnt)

                a[i] = '1'

            current_ones = 0
            cnt = 0
            for ai in a:
                if ai == '1':
                    current_ones += 1
                else:
                    cnt += current_ones
            res = max(res, cnt)

        print(res)


if __name__ == '__main__':
    main()

# 2: 1
# 3: 2
# 4: 3
# 5:
# 6: 7
# 7:
# 8: 13

# 1 0
# 1 1 0
# 1 0 1 0
# 1
# 1 1 0 0 1 0
