ans = 0


def main() -> None:
    def dfs(x: int, y: int) -> None:
        global ans
        if '2' == matrix[x][y] or '1' == matrix[x][y]:
            return
        else:
            matrix[x] = matrix[x][:y] + '2' + matrix[x][y + 1:]
            ans += 1
            if 0 < x:
                dfs(x - 1, y)
            if 29 > x:
                dfs(x + 1, y)
            if 0 < y:
                dfs(x, y - 1)
            if 39 > y:
                dfs(x, y + 1)

    global ans
    matrix = [input() for _i in range(30)]
    dfs(0, 0)

    print(matrix)
    print(ans)


if __name__ == '__main__':
    main()

'''
0000100010000001101010101001001100000011
0101111001111101110111100000101010011111
1000010000011101010110000000001011010100
0110101010110000000101100100000101001001
0000011010100000111111001101100010101001
0110000110000000110100000000010010100011
0100110010000110000000100010000101110000
0010011010100110001111001101100110100010
1111000111101000001110010001001011101101
0011110100011000000001101001101110100001
0000000101011000010011111001010011011100
0000100000011001000100101000111011101100
0010110000001000001010100011000010100011
0110110000100011011010011010001101011011
0000100100000001010000101100000000000010
0011001000001000000010011001100101000110
1110101000011000000100011001001100111010
0000100100111000001101001000001010010001
0100010010000110100001100000110111110101
1000001001100010011001111101011001110001
0000000010100101000000111100110010101101
0010110101001100000100000010000010110011
0000011101001001000111011000100111010100
0010001100100000011000101011000000010101
1001111010010110011010101110000000101110
0110011101000010100001000101001001100010
1101000000010010011001000100110010000101
1001100010100010000100000101111111111100
1001011010101100001000000011000110110000
0011000100011000010111101000101110110001
'''
