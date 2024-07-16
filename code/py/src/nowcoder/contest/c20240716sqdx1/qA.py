from collections import Counter


def main() -> None:
    # n, m, q = map(int, input().split())

    n = 3
    m = 3
    m2 = 0b1 << m
    ans = 0
    cnter = Counter()
    for i in range(0, m2):
        e = 4
        if 1 == i:
            ans += m2 ** e
            cnter[m2 ** e] += 1
            continue
        for j in range(0, m2):
            e = 3
            if 1 == j:
                ans += m2 ** e
                cnter[m2 ** e] += 1
                continue
            if 1 == i & j:
                ans += m2 ** e
                cnter[m2 ** e] += 1
                continue
            for k in range(0, m2):
                e = 2
                if 1 == k:
                    ans += m2 ** e
                    cnter[m2 ** e] += 1
                    continue
                if 1 == i & k or 1 == j & k:
                    ans += m2 ** e
                    cnter[m2 ** e] += 1
                    continue
                if 1 == i & j & k:
                    ans += m2 ** e
                    cnter[m2 ** e] += 1
                    continue
                for l in range(0, m2):
                    e = 1
                    if 1 == l:
                        ans += m2 ** e
                        cnter[m2 ** e] += 1
                        continue
                    if 1 == i & l or 1 == j & l or 1 == k & l:
                        ans += m2 ** e
                        cnter[m2 ** e] += 1
                        continue
                    if 1 == i & j & l or 1 == i & k & l or 1 == j & k & l:
                        ans += m2 ** e
                        cnter[m2 ** e] += 1
                        continue
                    if 1 == i & j & k & l:
                        ans += m2 ** e
                        cnter[m2 ** e] += 1
                        continue
                    for o in range(0, m2):
                        e = 0
                        if 1 == o:
                            ans += m2 ** e
                            cnter[m2 ** e] += 1
                            continue
                        if 1 == i & o or 1 == j & o or 1 == k & o or 1 == l & o:
                            ans += m2 ** e
                            cnter[m2 ** e] += 1
                            continue
                        if 1 == i & j & o or 1 == i & k & o or 1 == i & l & o or 1 == j & k & o or 1 == j & l & o or 1 == k & l & o:
                            ans += m2 ** e
                            cnter[m2 ** e] += 1
                            continue
                        if 1 == i & j & k & o or 1 == i & j & l & o or 1 == i & k & l & o or 1 == j & k & l & o:
                            ans += m2 ** e
                            cnter[m2 ** e] += 1
                            continue
                        if 1 == i & j & k & l & o:
                            ans += m2 ** e
                            cnter[m2 ** e] += 1
                            continue


    print(ans)
    print(cnter)


if __name__ == '__main__':
    main()

'''
m=1  1, 1, 1, 1, 1
m=2  1, 3, 9, 27, 81
m=3  1, 9, 69, 489, 3309
m=4  1, 27, 495, 7839, 114759
m=5  1, 81, 3441, 119265, 3722673
m=6  1, 243, 23559, 1769487, 


m=1  1/3, 1/3, 1/3, 1/3, 1/3
m=2  1/3, 1, 3, 9, 27
m=3  1/3, 3, 13, 163, 1103
m=4  1/3, 9, 165, 2613, 38253
m=5  1/3, 27, 1147, 39755, 1240891
m=6  1/3, 81, 7853, 589829

'''
