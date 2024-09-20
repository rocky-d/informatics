from collections import deque


def main() -> None:
    n = int(input())
    s = input()

    stk = deque()
    for char in s:
        if 'f' == char:
            stk.append(char)
        elif 'c' == char:
            if 0 < len(stk) and 'f' == stk[-1]:
                stk.pop()
            else:
                stk.append(char)
        elif 't' == char:
            stk.append(char)
        elif 'b' == char:
            if 0 < len(stk) and 't' == stk[-1]:
                stk.pop()
            else:
                stk.append(char)
        else:
            stk.append(char)
    print(len(stk))


if __name__ == '__main__':
    main()
