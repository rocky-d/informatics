def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))
    ops = input().split()

    for op in reversed(ops):
        num1, num2 = nums.pop(-1), nums.pop(-1)
        if '+' == op:
            nums.append(num2 + num1)
        elif '-' == op:
            nums.append(num2 - num1)
        elif '*' == op:
            nums.append(num2 * num1)
        else:  # elif '/' == op:
            if 0 == num1:
                print(f"ERROR: {num2}/0")
                break
            nums.append(num2 // num1)
    else:
        print(nums.pop(-1))


if __name__ == '__main__':
    main()
