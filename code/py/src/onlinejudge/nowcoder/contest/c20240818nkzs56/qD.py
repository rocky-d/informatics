def main() -> None:
    n = int(input())
    a = map(int, input().split())

    ans = -1
    a = sorted(a)
    for i in range(2, n):
        x, y, z = a[i - 2], a[i - 1], a[i]
        if x + y > z and x + z > y and z + y > x:
            ans = max(ans, x + y + z)
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
