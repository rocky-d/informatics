def main():
    triangle = [[1]]
    for i in range(int(input()) - 1):
        triangle += [[1]]
        for j in range(i):
            triangle[-1] += [triangle[-2][j] + triangle[-2][j + 1]]
        triangle[-1] += [1]

    for row in triangle:
        print(*row)


if __name__ == '__main__':
    main()
