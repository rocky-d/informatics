from bisect import bisect


def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    queues = []
    queues_len_max = 0
    waiting = n
    for num in nums:
        if waiting == num:
            waiting -= 1
            while 1 <= waiting:
                for i, queue_dec in enumerate(queues):
                    if waiting == queue_dec[0]:
                        if 1 == len(queue_dec):
                            del queues[i]
                        else:
                            del queue_dec[0]
                        waiting -= 1
                        break
                else:
                    break
        else:
            if 0 == len(queues) or queues[-1][-1] < num:
                queues.append([num])
                queues_len_max = max(queues_len_max, len(queues))
            else:
                queues[bisect(queues, num, key = lambda queue_dec: queue_dec[-1])].append(num)
    print(1 + queues_len_max)


if __name__ == '__main__':
    main()
