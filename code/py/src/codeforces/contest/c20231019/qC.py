def main() -> None:
    n, m = map(int, input().split())
    a_ls = list(map(int, input().split()))
    b_ls = list(map(int, input().split()))

    curr_dorm = 0
    curr_rooms = 0
    for b in b_ls:
        while b > curr_rooms:
            curr_rooms += a_ls[curr_dorm]
            curr_dorm += 1
        print(curr_dorm, a_ls[curr_dorm - 1] - (curr_rooms - b))


if __name__ == '__main__':
    main()
