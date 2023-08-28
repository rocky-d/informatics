def main() -> None:
    n = int(input())
    # input()
    sb_table = [list(map(int, input().split())) for _ in range(n)]
    print(sb_table)

    for i in range(n):
        init = sb_table[i]
        stack = [i]
        while stack:
            vertex = stack.pop()
            print(vertex)
            # for nei in range(vertex + 1, )



if __name__ == '__main__':
    main()
