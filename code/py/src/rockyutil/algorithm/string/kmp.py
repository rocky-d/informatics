def kmp(target: str, pattern: str) -> int:
    m, n = len(target), len(pattern)
    nxts = [0]
    lft, rit = 0, 1
    while rit < n:
        if pattern[lft] == pattern[rit]:
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
        if target[i] == pattern[j]:
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
    pass
