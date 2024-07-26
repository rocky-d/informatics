def main() -> None:
    n, q = map(int, input().split())
    a = input()
    b = input()
    lr = (map(int, input().split()) for _ in range(q))

    ans = []
    a_prefs = [[0] * 26 for _ in range(1 + n)]
    b_prefs = [[0] * 26 for _ in range(1 + n)]
    for i, (ai, bi) in enumerate(zip(a, b), start = 1):
        for j in range(26):
            a_prefs[i][j] = a_prefs[i - 1][j]
            b_prefs[i][j] = b_prefs[i - 1][j]
        a_prefs[i][ord(ai) - ord('a')] += 1
        b_prefs[i][ord(bi) - ord('a')] += 1
    for l, r in lr:
        al, ar = a_prefs[l - 1], a_prefs[r]
        bl, br = b_prefs[l - 1], b_prefs[r]
        ans.append(sum(abs((ar[i] - al[i]) - (br[i] - bl[i])) for i in range(26)) // 2)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
