from calendar import isleap


def is_leap_year(year):
    return 0 == year % 4 and 0 != year % 100 or 0 == year % 400


if __name__ == '__main__':
    print(all(isleap(year) == is_leap_year(year) for year in range(-1_000_000, +1_000_001)))
