def main() -> None:
    for _ in range(int(input())):
        n = int(input())
        negs = 0
        for s in input().split():
            ai = int(s)
            if 0 == ai:
                print('0')
                break
            elif ai < 0:
                negs += 1
        else:
            if 1 == negs % 2:
                print('0')
            else:
                print('1')
                print('1 0')


if __name__ == '__main__':
    main()
