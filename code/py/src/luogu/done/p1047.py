# def update_subway(u: int, v: int, subway: list[list[int]]):
#     for i in range(len(subway)):
#         if subway[i][0] <= u <= subway[i][1]:
#             if subway[i][1] < v:
#                 subway[i][1] = v
#             break
#         if subway[i][0] <= v <= subway[i][1]:
#             subway[i][0] = u
#             break
#         if u < subway[i][0] and subway[i][1] < v:
#             subway[i] = [u, v]
#             break
#     else:
#         subway += [[u, v]]
#
#
# def main() -> None:
#     l, m = map(int, input().split())
#
#     subway = []
#     for _ in range(m):
#         u, v = map(int, input().split())
#         update_subway(u, v, subway)
#
#     new_subway = []
#     for i in range(len(subway)):
#         update_subway(subway[i][0], subway[i][1], new_subway)
#     subway = new_subway
#
#     for part in subway:
#         l -= part[1] - part[0]
#     print(l + 1 - len(subway))


def main() -> None:
    l, m = map(int, input().split())
    table = sorted([list(map(int, input().split())) for _ in range(m)], key = lambda x: x[0])
    right = -1
    for u, v in table:
        if right < v:
            l -= v - max(u, right + 1) + 1
            right = v
    print(l + 1)


if __name__ == '__main__':
    main()
