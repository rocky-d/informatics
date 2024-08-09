def main() -> None:
    input()
    print('NO', flush = True)


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
