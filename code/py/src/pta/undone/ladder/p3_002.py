from bisect import insort_right, bisect_left
from collections import deque


def main() -> None:
    n = int(input())
    operations = [input() for _ in range(n)]

    ans = deque(maxlen = n)
    stack = deque()
    heap = []
    cnt = -1

    def push(num: int) -> None:
        stack.append(num)
        insort_right(heap, num)

    def pop() -> int:
        res = stack.pop()
        heap.pop(bisect_left(heap, res))
        return res

    def peek_median() -> int:
        return heap[cnt // 2]

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
