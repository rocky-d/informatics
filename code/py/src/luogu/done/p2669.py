def main():
    k = int(input())
    res = 0
    i = 1
    while True:
        if k > i:
            res += i ** 2
            k -= i
        else:
            res += i * k
            break
        i += 1
    print(res)


if __name__ == '__main__':
    main()
