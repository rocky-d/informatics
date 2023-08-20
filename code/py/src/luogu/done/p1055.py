def main():
    isbn = input()
    id = eval(f'({isbn[0]}+2*{isbn[2]}+3*{isbn[3]}+4*{isbn[4]}+5*{isbn[6]}+6*{isbn[7]}+7*{isbn[8]}+8*{isbn[9]}+9*{isbn[10]})%11')
    id = 'X' if 10 == id else str(id)
    print('Right' if id == isbn[-1] else isbn[:12] + id)


if __name__ == '__main__':
    main()
