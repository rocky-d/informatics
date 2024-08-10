def case() -> None:
    s = input()

    if s.endswith('?'):
        if 'PTA' in s:
            ans = 'Yes!'
        else:
            ans = 'No.'
    else:
        ans = 'enen'
    print(ans)


def main() -> None:
    for _ in range(int(input())):
        case()


if __name__ == '__main__':
    main()
