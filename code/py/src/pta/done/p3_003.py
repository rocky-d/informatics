def main() -> None:
    n = int(input())
    heads, groups = {}, {}
    hobbies = {}

    def find(a: int) -> int:
        if a == heads[a]:
            return a
        heads[a] = find(heads[a])
        return heads[a]

    def union(a: int, b: int) -> None:
        a_head, b_head = find(a), find(b)
        if a_head != b_head:
            if groups[a_head] < groups[b_head]:
                heads[a] = heads[a_head] = b_head
                groups[b_head] += groups.pop(a_head)
            else:
                heads[b] = heads[b_head] = a_head
                groups[a_head] += groups.pop(b_head)

    for person in range(1, 1 + n):
        heads[person] = person
        groups[person] = 1
        for h in input().split(maxsplit = 1)[1].split():
            if h in hobbies:
                union(person, hobbies[h])
            else:
                hobbies[h] = person
    print(len(groups))
    print(*sorted(groups.values(), reverse = True), sep = ' ')


if __name__ == '__main__':
    main()
