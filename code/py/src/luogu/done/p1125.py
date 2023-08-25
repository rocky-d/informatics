def main():
    prime100 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    count = {}
    for ch in input():
        count[ch] = count[ch] + 1 if count.get(ch) else 1
    diff = max(count_values := count.values()) - min(count_values)
    print(f'Lucky Word\n{diff}' if diff in prime100 else f'No Answer\n{0}')


if __name__ == '__main__':
    main()
