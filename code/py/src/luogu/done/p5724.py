def main():
    input()
    ls = sorted(list(map(int, input().split())))
    print(ls[-1] - ls[0])


if __name__ == '__main__':
    main()
