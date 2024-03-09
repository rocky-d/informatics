from bisect import insort_right, bisect_left
from collections import deque


def main() -> None:
    n = int(input())
    operations = [input() for _ in range(n)]

    ans = deque(maxlen = n)
    stk = deque()
    heap1, heap2 = [0], [100_001]
    cnt = -1

    def _adjust() -> None:
        while len(heap2) < len(heap1):
            heap2.insert(0, heap1.pop(-1))
        while len(heap1) < len(heap2):
            heap1.append(heap2.pop(0))

    def push(num: int) -> None:
        stk.append(num)
        if num < heap2[0]:
            insort_right(heap1, num)
        else:
            insort_right(heap2, num)
        _adjust()

    def pop() -> int:
        res = stk.pop()
        if res < heap2[0]:
            del heap1[bisect_left(heap1, res)]
        else:
            del heap2[bisect_left(heap2, res)]
        _adjust()
        return res

    def peek_median() -> int:
        return heap1[-1]

    for operation in operations:
        if operation.startswith('Pu'):
            push(int(operation.split()[1]))
            cnt += 1
        elif operation.startswith('Po'):
            if -1 == cnt:
                ans.append('Invalid')
            else:
                ans.append(pop())
                cnt -= 1
        else:  # elif operations.startswith('Pe'):
            if -1 == cnt:
                ans.append('Invalid')
            else:
                ans.append(peek_median())
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
