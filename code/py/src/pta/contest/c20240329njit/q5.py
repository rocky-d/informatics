from collections import Counter, deque


def main() -> None:
    n, m = map(int, input().split())
    photos = [frozenset(input().split(maxsplit = 1)[1].split()) for _ in range(m)]
    a, b = input().split()

    ans = deque()
    a_relations, b_relations = Counter(), Counter()
    a_relations[b], b_relations[a] = 0, 0
    for photo in photos:
        val = 1 / len(photo)
        if a in photo:
            for p in photo:
                if '-' == a[0] and '-' != p[0] or '-' != a[0] and '-' == p[0]:
                    a_relations[p] += val
        if b in photo:
            for p in photo:
                if '-' == b[0] and '-' != p[0] or '-' != b[0] and '-' == p[0]:
                    b_relations[p] += val
    a_items = sorted(a_relations.items(), key = lambda item: (-item[1], abs(int(item[0]))))
    b_items = sorted(b_relations.items(), key = lambda item: (-item[1], abs(int(item[0]))))
    if a_items[0][1] == a_relations[b] and b_items[0][1] == b_relations[a]:
        ans.append(a + ' ' + b)
    else:
        idx = 0
        a_len = len(a_items)
        a_max = a_items[0][1]
        a_ = a + ' '
        while idx < a_len and a_max == a_items[idx][1]:
            ans.append(a_ + a_items[idx][0])
            idx += 1
        idx = 0
        b_len = len(b_items)
        b_max = b_items[0][1]
        b_ = b + ' '
        while idx < b_len and b_max == b_items[idx][1]:
            ans.append(b_ + b_items[idx][0])
            idx += 1
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
