def main() -> None:
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    nums = sorted(((xa - xb) ** 2 + (ya - yb) ** 2, (xa - xc) ** 2 + (ya - yc) ** 2, (xb - xc) ** 2 + (yb - yc) ** 2))
    print('Yes' if nums[0] + nums[1] == nums[2] else 'No')


if __name__ == '__main__':
    main()
