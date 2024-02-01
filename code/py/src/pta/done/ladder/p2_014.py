from bisect import bisect


def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    queues = []
    queues_len_max = 0
    waiting = n
    q_heads = dict()
    for num in nums:
        if waiting == num:
            waiting -= 1
            while 1 <= waiting:
                if waiting in q_heads.keys():
                    index = q_heads.pop(waiting)
                    if 1 == len(queues[index]):
                        del queues[index]
                    else:
                        del queues[index][0]
                        q_heads[queues[index][0]] = index
                    waiting -= 1
                else:
                    break
            else:
                break
        else:
            if 0 == len(queues) or queues[-1][-1] < num:
                q_heads[num] = len(queues)
                queues.append([num])
                queues_len_max = max(queues_len_max, len(queues))
            else:
                queues[bisect(queues, num, key = lambda queue_dec: queue_dec[-1])].append(num)
    print(1 + queues_len_max)


if __name__ == '__main__':
    main()
