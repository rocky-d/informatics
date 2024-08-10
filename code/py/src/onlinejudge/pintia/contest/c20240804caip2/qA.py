import sys

inputs = sys.stdin.readlines()


def main() -> None:
    total = 0
    length = 0
    cnt = 0
    for line in inputs:
        i = 0
        while i < len(line):
            while i < len(line) and not line[i].isalnum():
                i += 1
            word = 0
            a, b, c = False, False, False
            while i < len(line) and line[i].isalnum():
                if line[i].isupper():
                    a = True
                elif line[i].islower():
                    b = True
                else:
                    c = True
                i += 1
                word += 1
            if 0 < word:
                cnt += 1
                length += word
                if a and b and c:
                    total += 5
                elif a and c or b and c:
                    total += 3
                elif a and b:
                    total += 1
    print(total)
    print(length, cnt)


if __name__ == '__main__':
    main()
