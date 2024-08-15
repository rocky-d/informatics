def main() -> None:
    al, ar = map(int, input().split())
    bl, br = map(int, input().split())

    if al > bl:
        al, bl = bl, al
        ar, br = br, ar
    if al <= bl and br <= ar:
        print((br - bl) + (0 if al == bl else 1) + (0 if ar == br else 1))
        return
    if al <= bl and ar < br:
        if al == bl:
            print(ar - al + 1)
            return
        else:
            print(max(0, ar - bl + 2))
            return


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
