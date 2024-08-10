from itertools import permutations, combinations


def main() -> None:
    n = int(input())
    digits = map(int, input().split())

    digits = ''.join(map(str, sorted(digits)))
    if 3 == n:
        nums = []
        for a, b, c in permutations(digits, r = 3):
            nums.append(int(a + b + c))
        nums_square = {num * num: num for num in nums}
        total = sum(nums_square.keys())
        half = total // 2
        for a, b, c in combinations(nums_square.keys(), r = 3):
            if a + b + c == half:
                print(nums_square[a], nums_square[b], nums_square[c], sep = '\n')
                break
    else:
        nums = []
        for a, b, c, d in permutations(digits, r = 4):
            nums.append(int(a + b + c + d))
        nums_square = {num * num: num for num in nums}
        total = sum(nums_square.keys())
        half = total // 2
        for ls in combinations(nums_square.keys(), r = 12):
            if sum(ls) == half:
                print(*(nums_square[num] for num in ls), sep = '\n')
                break


if __name__ == '__main__':
    main()
