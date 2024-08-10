def main() -> None:
    n = int(input())
    s = input()

    if s == 'yourname':
        s = 'xxx'
    password = list(s)

    for _ in range(n):
        for idx, char in enumerate(password):
            if char.isalpha():
                if char.isupper():
                    if char == 'Z':
                        password[idx] = 'A'
                    else:
                        password[idx] = chr(ord(char) + 1)
                else:
                    if char == 'a':
                        password[idx] = 'z'
                    else:
                        password[idx] = chr(ord(char) - 1)
        i = 0
        while i < len(password):
            while i < len(password) and not password[i].isalpha():
                i += 1
            j = i
            isupper = password[i].isupper()
            while i < len(password) and password[i].isalpha() and isupper is password[i].isupper():
                i += 1
            if 3 <= i - j:
                if isupper:
                    password[j:i] = [char.lower() for char in password[j:i]]
                else:
                    password[j:i] = [char.upper() for char in password[j:i]]
    print(s)
    print(''.join(password), end = '')


if __name__ == '__main__':
    main()
