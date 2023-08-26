def main():
    a, b, c, d = map(int, input().split())
    print(c - a if d >= b else c - a - 1, d - b if d >= b else d + 60 - b)


if __name__ == '__main__':
    main()
