def main() -> None:
    n = int(input())
    n_1 = n - 1
    b_ls = list(map(int, input().split()))
    if n in (1, 2):
        print(0)
        return
    possibles = []
    for start in range(b_ls[0] - 1, b_ls[0] + 2):
        for end in range(b_ls[-1] - 1, b_ls[-1] + 2):
            diff = end - start
            if 0 == abs(diff) % n_1:
                possibles.append((start, diff // n_1))

    len_possibles = len(possibles)
    possible_ans = [0 if b_ls[0] == possibles[_i][0] else 1 for _i in range(len_possibles)]
    possible_index = [_i for _i in range(len_possibles)]
    possible_last = [possibles[_i][0] for _i in range(len_possibles)]
    for b in b_ls[1:]:
        possible_index_copy = possible_index.copy()
        for index in possible_index_copy:
            if possibles[index][1] == b - possible_last[index]:
                possible_last[index] = b
            elif possibles[index][1] == b + 1 - possible_last[index]:
                possible_last[index] = b + 1
                possible_ans[index] += 1
            elif possibles[index][1] == b - 1 - possible_last[index]:
                possible_last[index] = b - 1
                possible_ans[index] += 1
            else:
                possible_index.remove(index)
    print(-1 if 0 == len(possible_index) else min([possible_ans[index] for index in possible_index]))


if __name__ == '__main__':
    main()
