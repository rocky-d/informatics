def main():
    n, m = map(int, input().split())
    
    if n % 2 == 1 and m % 2 == 0:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
