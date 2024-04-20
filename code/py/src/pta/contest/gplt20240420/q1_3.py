def main():
    a, b = map(int, input().split())

    if a == 0 or a == 1:
        if b == 0:
            if a == 0:
                print('biii')
                print('stop')
            else:
                print('dudu')
                print('move')
        else:
            print('-')
            if a == 0:
                print('stop')
            else:
                print('move')
    else:
        print('-')
        print('stop')


if __name__ == '__main__':
    main()
