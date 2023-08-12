def main():
    leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    non_leap = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    special_year = [1900]

    year, month = map(int, input().split())

    print(leap[month] if 0 == year % 4 and year not in special_year else non_leap[month])


if __name__ == '__main__':
    main()
