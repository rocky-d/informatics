def main() -> None:
    n, w = map(int, input().split())
    a_ls = list(map(int, input().split()))

    curr_people = 0
    min_people = 0
    max_people = w
    for a in a_ls:
        curr_people += a
        max_people = min(max_people, w - curr_people)
        min_people = max(min_people, -curr_people)
    if min_people <= max_people:
        print(max_people - min_people + 1)
    else:
        print(0)


if __name__ == '__main__':
    main()
