from heapq import heappush, heappop


def main() -> None:
    n, m = map(int, input().split())

    players = []
    for i in range(m):
        player = [0, 0, i]
        for j in range(n):
            x, y, z = map(int, input().split())
            if 1 == z:
                player[0] -= 1
                player[1] += y + (x - 1) * 20
        heappush(players, player)
    ans = [None] * m
    rank = 0
    lst_rank = 0
    lst_player = 1, -1
    while 0 < len(players):
        rank += 1
        player = heappop(players)
        if player[:2] != lst_player:
            ans[player[2]] = f"{rank}\n{-player[0]}\n{player[1]}"
            lst_rank = rank
            lst_player = player[:2]
        else:
            ans[player[2]] = f"{lst_rank}\n{-lst_player[0]}\n{lst_player[1]}"
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
