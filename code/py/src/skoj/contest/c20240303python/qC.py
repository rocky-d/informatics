def main() -> None:
    budgets = []
    for _ in range(12):
        budgets.append(int(input().strip()))

    bank = 0
    balance = 0
    for i, budget in enumerate(budgets, 1):
        balance += 300
        if balance < budget:
            ans = -i
            break
        temp = 100 * ((balance - budget) // 100)
        bank += temp
        balance -= temp + budget
    else:
        ans = balance + int(1.2 * bank)
    print(ans)


if __name__ == '__main__':
    main()
