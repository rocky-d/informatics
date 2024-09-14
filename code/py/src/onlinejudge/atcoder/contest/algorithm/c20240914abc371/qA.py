def main() -> None:
    sab, sac, sbc = input().split()

    if '<' == sab:
        if '<' == sac:
            if '<' == sbc:
                ans = 'B'
            else:
                ans = 'C'
        else:
            if '<' == sbc:
                ans = None
            else:
                ans = 'A'
    else:
        if '<' == sac:
            if '<' == sbc:
                ans = 'A'
            else:
                ans = None
        else:
            if '<' == sbc:
                ans = 'C'
            else:
                ans = 'B'
    print(ans)


if __name__ == '__main__':
    main()
