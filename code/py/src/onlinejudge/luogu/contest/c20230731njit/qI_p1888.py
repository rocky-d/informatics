def main():
    abc = sorted(map(int, input().split()))
    for i in range(abc[0], 0, -1):
        if 0 == abc[0] % i and 0 == abc[2] % i:
            print(f'{abc[0] // i}/{abc[2] // i}')
            break


if __name__ == '__main__':
    main()
