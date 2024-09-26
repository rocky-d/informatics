abc = 'abcdefghijklmnopqrstuvwxyz'
def main():
    n = int(input())
    passwords = (input() for _ in range(n))

    ans = []
    for word in passwords:
        cnter = {}
        for char in word:
            cnter[char] = cnter.get(char, 0) + 1
        valid_chars = set(abc) | set(abc.upper()) | set('0123456789') | set('*#')

        if not (6 <= len(word) and all(char in valid_chars for char in cnter.keys())):
            ans.append(0)
            continue

        if not (any(char in cnter.keys() for char in abc+ abc.upper()) and any(char in cnter.keys() for char in '0123456789') and any(char in cnter.keys() for char in '*#')):
            ans.append(0)
            continue
        if any(2 < cnt for cnt in cnter.values()):
            ans.append(1)
            continue
        ans.append(2)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
