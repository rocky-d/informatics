def case() -> None:
    a_, b_ = map(int, input().split())
    target = 1 if a_ < b_ else 0
    take = 0 if a_ < b_ else 1
    red_win, red_lose = 0.0, 0.0
    purple_win, purple_lose = 0.0, 0.0
    queue = [[a_, b_ - 1, 1.0] if 0 == take else [a_ - 1, b_, 1.0]]
    if 0 == queue[0][0] or 0 == queue[0][1]:
        red_win = 0.0
    else:
        in_queue = set()
        in_queue.add((queue[0][0], queue[0][1]))
        done = set()
        while 0 < len(queue):
            a, b, p = queue.pop(0)
            sum_ab = a + b
            in_queue.remove((a, b))

            son1 = [a - 1, b, p * a / sum_ab]
            if 0 == son1[0]:
                if 0 == son1[take]:
                    red_win += son1[2]
                else:
                    ...
            else:
                son1[take] -= 1
                if 0 == son1[take]:
                    if 1 < son1[target]:
                        red_win += son1[2]
                    else:
                        ...
                else:
                    if (son1[0], son1[1]) in in_queue:
                        for i in range(len(queue)):
                            if queue[i][0] == son1[0] and queue[i][1] == son1[1]:
                                queue[i][2] += son1[2]
                                break
                    else:
                        in_queue.add((son1[0], son1[1]))
                        queue.append(son1)

            son2 = [a, b - 1, p * b / sum_ab]
            if 0 == son2[1]:
                if 0 == son2[take]:
                    red_win += son2[2]
                else:
                    ...
            else:
                son2[take] -= 1
                if 0 == son2[take]:
                    if 1 < son2[target]:
                        red_win += son2[2]
                    else:
                        ...
                else:
                    if (son2[0], son2[1]) in in_queue:
                        for i in range(len(queue)):
                            if queue[i][0] == son2[0] and queue[i][1] == son2[1]:
                                queue[i][2] += son2[2]
                                break
                    else:
                        in_queue.add((son2[0], son2[1]))
                        queue.append(son2)
    print(red_win)


def main() -> None:
    for _ in range(int(input())):
        case()


if __name__ == '__main__':
    main()
