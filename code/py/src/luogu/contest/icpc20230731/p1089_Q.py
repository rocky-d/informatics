def main():
    earning = 300
    deposit_base = 100
    deposit = 0
    pocket = 0
    for month in range(1, 13):
        budget = int(input())
        pocket += earning - budget
        if pocket < 0:
            print(f'-{month}')
            break
        else:
            deposit += pocket // deposit_base
            pocket %= deposit_base
    else:
        print(pocket + 120 * deposit)


if __name__ == '__main__':
    main()
