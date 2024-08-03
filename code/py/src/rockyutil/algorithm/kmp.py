def kmp(s, sub):
    n, m = len(s), len(sub)
    nxts = [0]
    lft, rit = 0, 1
    while rit < m:
        if sub[lft] == sub[rit]:
            lft += 1
            rit += 1
            nxts.append(lft)
        else:
            if 0 < lft:
                lft = nxts[lft - 1]
            else:
                rit += 1
                nxts.append(0)
    i, j = 0, 0
    while i < n:
        if s[i] == sub[j]:
            i += 1
            j += 1
            if j == m:
                ans = i - j
                break
        else:
            if 0 < j:
                j = nxts[j - 1]
            else:
                i += 1
    else:
        ans = -1
    return ans


if __name__ == '__main__':
    s, sub = 'abbcd', 'bc'

    print(s.index(sub))
    print(s.find(sub))
    print(kmp(s, sub))
