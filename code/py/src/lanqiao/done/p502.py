def main():
    n = int(input().strip())
    ls = []
    b = 0
    a = 0
    for _ in range(n):
        ls.append(int(input().strip()))
        if 60 <= ls[-1]:
            b += 1
            if 85 <= ls[-1]:
                a += 1
    print(f'{round(b * 100 / n)}%')
    print(f'{round(a * 100 / n)}%')


if __name__ == '__main__':
    main()
