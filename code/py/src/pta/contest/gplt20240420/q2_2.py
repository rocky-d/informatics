from bisect import insort_left


def main():
    n = int(input())
    abbrmap = {}
    for _ in range(n):
        sent = input()
        abbr = ''.join(map(lambda s: s[0], sent.split()))
        if abbr in abbrmap:
            insort_left(abbrmap[abbr], sent)
        else:
            abbrmap[abbr] = [sent]
    for _ in range(int(input())):
        sent = input()
        abbr = ''.join(map(lambda s: s[0], sent.split()))
        if abbr in abbrmap:
            print(*abbrmap[abbr], sep = '|')
        else:
            print(sent)


if __name__ == '__main__':
    main()
