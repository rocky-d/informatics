def main() -> None:
    year = int(input())

    print(
        'Yes'
        if 0 == year % 4
        and 0 != year % 100
        or 0 == year % 400
        and 0 != year % 3200
        or 0 == year % 172800
        else 'No'
    )


if __name__ == '__main__':
    main()
