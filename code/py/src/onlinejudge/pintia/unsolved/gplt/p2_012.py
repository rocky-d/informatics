from collections import deque
from heapq import heappush


def main() -> None:
    n, m = map(int, input().split())
    nums = map(int, input().split())
    propositions = []
    for _ in range(m):
        propositions.append(input().split())

    ans = deque(maxlen = m)
    heap_min = []
    for num in nums:
        heappush(heap_min, num)
    nums_idxes = {str(val): idx for idx, val in enumerate(heap_min, 1)}
    for proposition in propositions:
        if 4 == len(proposition):
            ans.append('T' if 1 == nums_idxes[proposition[0]] else 'F')
        elif 5 == len(proposition):
            ans.append('T' if 1 == abs(nums_idxes[proposition[0]] - nums_idxes[proposition[2]]) else 'F')
        else:  # elif 6 == proposition_len:
            if 'the' == proposition[2]:
                ans.append('T' if nums_idxes[proposition[-1]] - 2 * nums_idxes[proposition[0]] in (0, 1) else 'F')
            else:  # elif 'a' == proposition[2]:
                ans.append('T' if nums_idxes[proposition[0]] - 2 * nums_idxes[proposition[-1]] in (0, 1) else 'F')
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
