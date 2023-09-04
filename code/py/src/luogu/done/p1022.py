def main() -> None:
    left0, right0 = input().split('=')

    if left0[0] == '-':
        left0 = '0' + left0
    elif left0[0] == '+':
        left0 = left0[1:]
    if right0[0] == '-':
        right0 = '0' + right0
    elif right0[0] == '+':
        right0 = right0[1:]

    ch: str = ''
    left1: list = []
    right1: list = []

    for x in [x.split('-') for x in left0.split('+')]:
        if x[0][-1].isalpha():
            ch = x[0][-1]
            left1 += ['+' + x[0][:-1] if len(x[0]) > 1 else '1']
        else:
            right1 += ['-' + x[0]]
        for xx in x[1:]:
            if xx[-1].isalpha():
                ch = xx[-1]
                left1 += ['-' + xx[:-1] if len(xx) > 1 else '1']
            else:
                right1 += ['+' + xx]

    for x in [x.split('-') for x in right0.split('+')]:
        if x[0][-1].isalpha():
            ch = x[0][-1]
            left1 += ['-' + x[0][:-1] if len(x[0]) > 1 else '1']
        else:
            right1 += ['+' + x[0]]
        for xx in x[1:]:
            if xx[-1].isalpha():
                ch = xx[-1]
                left1 += ['+' + xx[:-1] if len(xx) > 1 else '1']
            else:
                right1 += ['-' + xx]

    print(f'{ch}={round(eval("".join(right1)) / eval("".join(left1)), 3):.3f}')


if __name__ == '__main__':
    main()
