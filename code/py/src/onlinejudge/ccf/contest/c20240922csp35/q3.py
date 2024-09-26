import sys


PATCH_IS_DAMAGED = 'Patch is damaged.'

lines = sys.stdin.read().split('\n')
while 0 == len(lines[-1]):
    lines.pop(-1)

def main():
    n = int(lines[0])
    origin = (lines[idx] for idx in range(1, 1 + n))

    origin = [None] + list(origin)
    lo, hi = 1 + n, len(lines)
    for idx in range(lo, hi):
        line = lines[idx]
        if '@' != line[0]:
            continue
        lo = idx
        break
    else:
        print(PATCH_IS_DAMAGED)
        # print(1)
        return
    idx = lo
    blocks = []
    while idx < hi:
        line = lines[idx]
        if not(15 <= len(line) and '@@ ' == line[:3] and line[-3:] == ' @@'):
            print(PATCH_IS_DAMAGED)
            # print(2)
            return
        line_lft, line_rit = line[3:-3].split(' ', maxsplit=1)
        NN, MM = line_lft.split(',', maxsplit=1)
        if not ('-' == NN[0] and NN[1:].isdigit() and MM.isdigit()):
            print(PATCH_IS_DAMAGED)
            # print(3)
            return
        NN = int(NN[1:])
        MM = int(MM)
        nn, mm = line_rit.split(',', maxsplit=1)
        if not ('+' == nn[0] and nn[1:].isdigit() and mm.isdigit()):
            print(PATCH_IS_DAMAGED)
            # print(4)
            return
        nn = int(nn[1:])
        mm = int(mm)
        if 0 < len(blocks):
            header = blocks[-1][0]
            if not (NN >= header[0] + header[1]):
                print(PATCH_IS_DAMAGED)
                # print(5)
                return
        block = [[NN, MM, nn, mm]]
        idx += 1
        content_lines = 0
        new_lines = 0
        while idx < hi and '@' != lines[idx][0]:
            line = lines[idx]
            char = line[0]
            if '#' != char:
                if not (char in '-+ '):
                    print(PATCH_IS_DAMAGED)
                    # print(6)
                    return
                if '-' == char:
                    content_lines += 1
                elif '+' == char:
                    new_lines += 1
                else:
                    content_lines += 1
                    new_lines += 1
                block.append(line)
            idx += 1
        if not (MM == content_lines and mm == new_lines):
            print(PATCH_IS_DAMAGED)
            # print(7)
            return
        blocks.append(block)
    # if 0 == len(blocks):
    #     print(PATCH_IS_DAMAGED)
    #     return
    # vis = [None] + [False] * n
    thenew = [None]
    lst = 1
    NN_ofst = 0
    for bi, block in enumerate(blocks):
        NN, MM, nn, mm = block[0]
        NN += NN_ofst
        for ofst in range(MM):
            ofst = -ofst
            if 0 < bi:
                if not (NN + ofst >= blocks[bi - 1][0][0] + blocks[bi - 1][0][1]):
                    continue
            j = 0
            j += 1
            while j < len(block) and '+' == block[j][0]:
                j += 1
            for i in range(NN + ofst, NN + ofst + MM):
                if origin[i] != block[j][1:]:
                    ok = False
                    break
                j += 1
                while j < len(block) and '+' == block[j][0]:
                    j += 1
            else:
                ok = j == len(block)
            if ok:
                break
            ofst = -ofst
            if 0 < bi:
                if not (NN + ofst >= blocks[bi - 1][0][0] + blocks[bi - 1][0][1]):
                    continue
            j = 0
            j += 1
            while j < len(block) and '+' == block[j][0]:
                j += 1
            for i in range(NN + ofst, NN + ofst + MM):
                if origin[i] != block[j][1:]:
                    ok = False
                    break
                j += 1
                while j < len(block) and '+' == block[j][0]:
                    j += 1
            else:
                ok = j == len(block)
            if ok:
                break
        else:
            print(PATCH_IS_DAMAGED)
            # print(9)
            return
        for ii in range(lst, NN + ofst):
            thenew.append(origin[ii])
        lst = NN + ofst + MM
        for j in range(1, len(block)):
            line = block[j]
            if '-' == line[0]:
                continue
            thenew.append(line[1:])
        block[0][0] += NN_ofst
        NN_ofst += ofst
    for ii in range(lst, len(origin)):
        thenew.append(origin[ii])
    del thenew[0]
    print(*thenew, sep='\n')


if __name__ == '__main__':
    main()
