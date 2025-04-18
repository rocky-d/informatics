from itertools import permutations


def main() -> None:
    n = int(input())

    for chars in permutations('ABCD'[:n]):
        print('+'.join(chars), 'Problem')


main()
