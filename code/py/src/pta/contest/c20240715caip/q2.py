def main():
    n = int(input())
    teams = [0] * 21

    rating = [None, 12, 9, 7, 5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    for _ in range(n):
        i = 0
        for p, k in (map(int, input().split()) for _ in range(20)):
            i += 1
            teams[i] += rating[p] + k
    for i in range(1, 21):
        print(i, teams[i])


if __name__ == '__main__':
    main()
