def main():
    isbn = input()
    isbn_id = eval(f'({isbn[0]}+2*{isbn[2]}+3*{isbn[3]}+4*{isbn[4]}+5*{isbn[6]}+6*{isbn[7]}+7*{isbn[8]}+8*{isbn[9]}+9*{isbn[10]})%11')
    isbn_id = 'X' if 10 == isbn_id else str(isbn_id)
    print('Right' if isbn_id == isbn[-1] else isbn[:12] + isbn_id)


if __name__ == '__main__':
    main()
