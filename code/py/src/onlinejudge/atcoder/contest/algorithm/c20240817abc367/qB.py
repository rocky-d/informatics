def main() -> None:
    x = float(input())

    ans = str(x)
    if ans.endswith('.0'):
        ans = ans[:-2]
    print(ans)


if __name__ == '__main__':
    main()
