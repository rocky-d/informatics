from collections import Counter


def main() -> None:
    n = int(input())
    matches = ((map(int, input().split()) for _ in range(20)) for _ in range(n))

    scoremap = [None, 25, 21, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    teams = Counter()
    for match in matches:
        for c, p in match:
            score = scoremap[p]
            teams[c] += score
    result = sorted(teams.items(), key = lambda item: (-item[1], item[0]))
    print('\n'.join(map(lambda item: f"{item[0]} {item[1]}", result)))


if __name__ == '__main__':
    main()
