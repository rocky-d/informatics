def main() -> None:
    a, b, c = map(int, input().split())

    if b < c:
        ans = 'No' if b < a < c else 'Yes'
    else:  # elif b > c:
        ans = 'Yes' if c < a < b else 'No'
    print(ans)


if __name__ == '__main__':
    main()
