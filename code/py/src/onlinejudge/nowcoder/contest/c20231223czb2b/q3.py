def primes_before(n):
    res = set()
    tags = [False for _ in range(2)] + [True for _ in range(2, n)]
    for i in range(2, n):
        if tags[i]:
            res.add(i)
            for composite in range(i * i, n, i):
                tags[composite] = False
    return res


def main() -> None:
    primes = primes_before(200000)
    n = int(input())
    a = list(map(int, input().split()))
    if n < 3:
        if 2 == n:
            if a[0] + a[1] in primes:
                print(1)
            else:
                print(-1)
        else:
            print(-1)
        return
    loss = []
    for i in range(n - 1):
        if a[i] + a[i + 1] not in primes:
            loss.append(i)
    if 0 == len(loss):
        match, ans = 0, n
        if a[0] + a[2] in primes:
            match += 1
            ans = 0
        if a[-1] + a[-3] in primes:
            match += 1
            ans = n - 1
            if match == 2:
                print(-1)
                return
        for i in range(1, n - 2):
            if a[i - 1] + a[i + 1] in primes and a[i] + a[i + 2] in primes:
                match += 1
                ans = i
                if match == 2:
                    print(-1)
                    return
        if match == 1:
            print(ans + 1)
        else:
            print(-1)
    elif 1 == len(loss):
        p = loss[0]
        ok1, ok2 = True, True
        if p - 1 > -1:
            if a[p - 1] + a[p + 1] not in primes:
                ok1 = False
        else:
            ok1 = False
        if p - 2 > -1:
            if a[p - 2] + a[p] not in primes:
                ok1 = False
        if p + 2 < n:
            if a[p] + a[p + 2] not in primes:
                ok2 = False
        else:
            ok2 = False
        if p + 3 < n:
            if a[p + 1] + a[p + 3] not in primes:
                ok2 = False
        if (not ok1 and ok2) or (ok1 and not ok2):
            if ok1:
                print(p)
            else:
                print(p + 2)
        else:
            print(-1)
    elif 2 == len(loss):
        if loss[1] - loss[0] == 2 and a[loss[0]] + a[loss[1]] in primes and a[loss[0] + 1] + a[loss[1] + 1] in primes:
            print(loss[1])
        else:
            print(-1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
