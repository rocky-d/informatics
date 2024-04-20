def main() -> None:
    for _i_ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        new_arr = [arr[0]]
        for i in range(1, n):
            if arr[i - 1] == arr[i]:
                continue
            else:
                new_arr.append(arr[i])
        # print(new_arr)
        if len(new_arr) < 3:
            print('YES')
        else:
            lens = len(new_arr)
            flag = lens
            new_flag = lens
            for i in range(1, lens):
                if new_arr[i - 1] < new_arr[i]:
                    flag = i
                    break
            for i in range(flag, lens):
                if new_arr[i - 1] > new_arr[i]:
                    new_flag = i
                    break
            if new_flag == lens:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    main()
