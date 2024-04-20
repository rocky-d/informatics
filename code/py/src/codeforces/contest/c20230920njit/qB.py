def main() -> None:
    tests = int(input())
    alp = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
           'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
           'z': 26}
    while tests > 0:
        tests -= 1
        n = int(input())
        word = input()
        max_ = 0
        for ch in word:
            max_ = max(max_, alp[ch])
        print(max_)


if __name__ == '__main__':
    main()
