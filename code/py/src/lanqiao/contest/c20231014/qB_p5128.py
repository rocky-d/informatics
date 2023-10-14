def main() -> None:
    for _t in range(int(input().split()[1])):
        num = 1
        for step in input():
            num *= 2
            if 'L' == step:
                num -= 1
        print(num)


if __name__ == '__main__':
    main()

'''
         1
       1   2
    1   2 3   4
 1  2 3 4 5 6 7  8
'''
