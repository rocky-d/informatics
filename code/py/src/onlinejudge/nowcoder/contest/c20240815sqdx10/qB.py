class pair(object):
    def __init__(self, lft, rit):
        self.lft = lft
        self.rit = rit


def main() -> None:
    n, q = map(int, input().split())
    s = (input() for _ in range(n))
    queries = (input() for _ in range(q))

    dct = {}
    for si in s:
        si, var = si.split(' ')
        dct[var[:-1]] = si
    for qi in queries:
        qs = qi.split('.')
        var = qs.pop(0)
        if 0 == len(qs):
            print(dct[var])
            continue
        si = dct[var]
        si = si.replace('<', '(\'')
        si = si.replace('>', '\')')
        si = si.replace(',', '\',\'')
        exec('x=' + si)


if __name__ == '__main__':
    main()
