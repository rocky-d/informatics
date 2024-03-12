def kmp(s, patt):
    m, n = len(s), len(patt)
    nxts = [0]
    lft, rit = 0, 1
    while rit < n:
        if patt[lft] == patt[rit]:
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
    while i < m:
        if s[i] == patt[j]:
            i += 1
            j += 1
            if j == n:
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
    print(kmp(s = 'abbcd', patt = 'bc'))
