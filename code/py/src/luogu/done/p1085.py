def main():
    max_day = 0
    max_val = 8
    for day in range(1, 8):
        tmp = sum(map(int, input().split()))
        if max_val < tmp:
            max_day = day
            max_val = tmp
    print(max_day)


if __name__ == '__main__':
    main()
