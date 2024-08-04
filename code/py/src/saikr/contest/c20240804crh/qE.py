def main() -> None:
    h, w, x1, y1, x2, y2 = map(int, input().split())

    if x1 >= x2:
        print('Draw')
        return
    diff = x2 - x1
    if 0b1 == 0b1 & diff:  # A -> B
        print(x1, x2, y1, y2)
    else:  # B -> A
        ...


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
