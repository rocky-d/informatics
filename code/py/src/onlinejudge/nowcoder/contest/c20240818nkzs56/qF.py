def main() -> None:
    n = int(input())
    s = input()
    t = input()

    lcp, idx = 0, None
    for i in range(n, 0, -1):
        s_ = s[i - 1::-1] + s[i:]
        if s_[:lcp] == t[:lcp]:
            j = lcp
            while j < n and s_[j] == t[j]:
                j += 1
            lcp, idx = j, i
    print(lcp, idx)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
