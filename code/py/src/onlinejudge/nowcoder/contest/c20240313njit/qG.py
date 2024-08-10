from collections import deque


def main() -> None:
    boolean = input()
    n = int(input())
    d = list(map(int, input().split()))
    ans = deque(maxlen = n)
    if 'F' == boolean[0]:
        stk_inc = deque([0])
        for di in d:
            while stk_inc[-1] > di:
                stk_inc.pop()
            stk_inc.append(di)
            ans.append(len(stk_inc) - 1)
    else:
        stk_inc = deque([0])
        for di in reversed(d):
            while stk_inc[-1] > di:
                stk_inc.pop()
            stk_inc.append(di)
            ans.appendleft(len(stk_inc) - 1)
    print(*ans)


if __name__ == '__main__':
    main()
