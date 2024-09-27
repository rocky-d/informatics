from bisect import bisect_left, bisect_right


def main():
    n, m, k = map(int, input().split())
    c = map(int, input().split())
    xlr = (map(int, input().split()) for _ in range(k))

    c = [None] + list(c)
    if all(i == c[i] for i in range(1, 1 + n)):
        ans = []
        woods = [[(1, n)]]
        for x, l, r in xlr:
            wood_lst, wood = woods[x], []
            idx1 = bisect_left(wood_lst, (l, 0))
            idx2 = bisect_right(wood_lst, ())
        return
    ans = []
    woods = [None] + [{i: c[i] for i in range(1, 1 + n)}]
    for x, l, r in xlr:
        wood_lst, wood = woods[x], {}
        for idx in range(l, r + 1):
            if idx not in wood_lst.keys():
                continue
            wood[idx] = wood_lst[idx]
            del wood_lst[idx]
        if 0 == len(wood):
            ans.append('0 0')
        else:
            cnt = 1
            ls = sorted(wood.keys())
            for i in range(1, len(ls)):
                lst, nxt = ls[i - 1], ls[i]
                if wood[lst] == wood[nxt]:
                    continue
                cnt += 1
            ans.append(' '.join(map(str, (len(frozenset(wood.values())), cnt))))
        woods.append(wood)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
