def main() -> None:
    n = int(input())
    gaps = input().split()
    m = int(input())
    fragments = [input().split()[1:] for _ in range(m)]

    ans = []
    seen = set()

    def dfs(index, seq):
        if index == len(gaps) - 1:
            for item in seq:
                ans.append(item)
            return True
        for i, fragment in enumerate(fragments, 1):
            if i in seen:
                continue
            if fragment[0] == gaps[index]:
                if fragment == gaps[index:index + len(fragment)]:
                    seen.add(i)
                    if dfs(index + len(fragment) - 1, seq + [i]):
                        return True
                    seen.remove(i)
        return False

    dfs(0, [])
    print(*ans)


if __name__ == '__main__':
    main()
