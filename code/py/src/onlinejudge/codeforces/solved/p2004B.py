def main() -> None:
    al, ar = map(int, input().split())
    bl, br = map(int, input().split())

    if al > bl:
        al, bl = bl, al
        ar, br = br, ar
    if al == bl:
        if ar < br:
            ans = ar - al + 1
        elif ar > br:
            ans = br - bl + 1
        else:  # elif ar == br:
            ans = ar - al
    else:  # elif al < bl:
        if ar < br:
            ans = max(1, ar - bl + 2)
        elif ar > br:
            ans = br - bl + 2
        else:  # elif ar == br:
            ans = br - bl + 1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
