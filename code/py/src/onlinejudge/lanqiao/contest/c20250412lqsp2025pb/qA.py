def main():
    life = 2025
    round = 0
    while 0 < life:
        round += 1
        life -= 5
        if 1 == round % 2:
            life -= 15
        else:
            life -= 2
        if 1 == round % 3:
            life -= 2
        elif 2 == round % 3:
            life -= 10
        else:
            life -= 7
    round += 1
    print(round)


main()
# 104
