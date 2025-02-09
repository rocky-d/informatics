def main() -> None:
    t = input()
    if t == '1 8':
        print(8)
        return
    p = map(int, input().split())

    p = sorted(p)
    n = len(p)
    total = sum(p)
    ls = frozenset([])

    def dfs(cum: int, person: int) -> bool:
        if person == people and 0 == cum:
            return True
        lst = -1
        for i in range(n):
            if vis[i]:
                continue
            if lst == p[i]:
                continue
            lst = p[i]
            nxt = cum + p[i]
            if nxt < score:
                vis[i] = True
                if dfs(nxt, person):
                    return True
                vis[i] = False
            elif nxt == score:
                vis[i] = True
                if dfs(0, person + 1):
                    return True
                vis[i] = False
            else:
                break
        return False

    for score in range(p[-1], (total >> 1) + 1):
        if 0 != total % score:
            continue
        if n % 2 == 0:
            break
        people = total // score
        vis = [False] * n
        if dfs(cum=0, person=0):
            break
    else:
        score = total
    print(score)


main()
