def main() -> None:
    n = int(input())
    buttons = map(int, input().split())

    buttons = list(buttons)
    i = 0
    while i < n:
        start = buttons[i] + 15
        while i < n and buttons[i] < start:
            i += 1
        end = start + 30
        if i < n and buttons[i] < end:
            end += 15
            i += 1
        while i < n and buttons[i] < end:
            i += 1
        print(start, end - 1)


if __name__ == '__main__':
    main()
