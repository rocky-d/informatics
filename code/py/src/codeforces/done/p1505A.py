def main() -> None:
    q = input()

    print('NO', flush = True)


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
