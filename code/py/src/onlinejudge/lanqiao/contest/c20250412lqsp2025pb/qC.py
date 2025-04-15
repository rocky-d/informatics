def main():
    char = 'Q'
    w, h, v = map(int, input().split())

    lines = []
    line = char * w
    for i in range(h):
        lines.append(line)
    line = char * (v + w)
    for i in range(w):
        lines.append(line)
    print('\n'.join(lines))


main()
