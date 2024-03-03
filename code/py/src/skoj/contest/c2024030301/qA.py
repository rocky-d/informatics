def main() -> None:
    passwords = input()

    ans = []
    chars = frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$')
    for password in passwords.split(','):
        password_set = frozenset(password)
        if 0 == len(password_set - chars) and 6 <= len(password) <= 12:
            nums = 0
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char in password_set:
                    nums += 1
                    break
            for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if char in password_set:
                    nums += 1
                    break
            for char in '0123456789':
                if char in password_set:
                    nums += 1
                    break
            if 2 <= nums:
                for char in '!@#$':
                    if char in password_set:
                        ans.append(password)
                        break
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
