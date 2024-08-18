def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a)
    for i in range(n - 1, 1, -1):
        x, y, z = a[i], a[i - 1], a[i - 2]
        if x + y > z and x + z > y:
            ans = x + y + z
            break
    else:
        ans = -1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
