import os
import time
from tkinter import *


# **********************************************************************************************************************


PROJECT_NAME = 'Decipher'
PROJECT_VERSION = '3.2.2'
PROJECT_TITLE = PROJECT_NAME + ' (' + PROJECT_VERSION + ')'

START_DATE = '11th October 2022'
END_DATE = '15th October 2022'

AUTHOR_NAME = 'Rocky Haotian Du'
CLASS_NUMBER = 211
STUDENT_ID_NJIT = 202211230
STUDENT_ID_UO = 2780823

ENCODING_MODE = 'UTF-8'
EXPLORER_MODE = 'open'  # 'open', 'explore'
WORK_DIRECTORY = '.\\' + PROJECT_NAME + ' - ' + AUTHOR_NAME + '\\'
CIPHERTEXT_TXT_NAME = 'ciphertext.txt'
SPACES = '  '
DEFAULT_RESULT = '   . . . '
AUTHOR_LABEL = \
    '----- This is made by -----\n\n' \
    '  Author :\n' \
    '        ' + AUTHOR_NAME + '\n\n' \
    '  Class Number :\n' + \
    '        ' + str(CLASS_NUMBER) + '\n\n' \
    '  Student ID :\n' + \
    '        ' + str(STUDENT_ID_NJIT) + ' (NJIT)\n' \
    '        ' + str(STUDENT_ID_UO) + ' (UO)\n'
ENCIPHERED_LABEL = \
    'DX DUUDESBF KDC EFBDUB D MQTS LBDUGFQXN D EHFZHFDUB YHNH DIDQYDAYB LFHK UOB UDFNBUT\n' \
    'WBATQUB UOB DUUDESBF UOBX YBDIBT UOB MQTS HX UOB LYHHF HL DX BYBIDUHF HF THKBWOBFB QX\n' \
    'UOB YHAAC HL UOB UDFNBU EHKZDXC DX GXSXHWQXN BKZYHCBB KDC LQXM QU DXM QXTBFU UOB\n' \
    'MQTS QXUH D EHKZGUBF UH TDUQTLC UOBQF EGFQHTQUC HF THKBHXB BYTB KDC LQXM QU DXM\n' \
    'FBUGFX QU UH UOB EHKZDXC QX DXC EDTB PGTU QXTBFUQXN UOB MQTS QXUH D EHKZGUBF QXTUDYYT\n' \
    'KDYWDFB NQIQXN DUUDESBFT DEEBTT UH UOB BKZYHCBBT EHKZGUBF DXM ZBFODZT UOB UDFNBU\n' \
    'EHKZDXCT QXUBFXDY EHKZGUBF XBUWHFS'
# ENCIPHERED_LABEL = \
#     'UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXU\n' \
#     'ZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ'

LOWER_ALPHABET = \
    ('?',
     'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n',
     'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
UPPER_ALPHABET = \
    ('?',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


# **********************************************************************************************************************


def check_dir():
    if not os.path.isdir(WORK_DIRECTORY):
        os.mkdir(WORK_DIRECTORY)
        print('>>> ' + WORK_DIRECTORY + ' [made]')


def read():
    check_dir()
    try:
        with open(WORK_DIRECTORY + CIPHERTEXT_TXT_NAME, 'r', encoding = ENCODING_MODE) as checker:
            has_capital = False
            for letter in checker.read():
                if letter.isupper():
                    has_capital = True
                    break
            if not has_capital:
                raise IOError
        with open(WORK_DIRECTORY + CIPHERTEXT_TXT_NAME, 'r', encoding = ENCODING_MODE) as reader:
            global ENCIPHERED_LABEL
            ENCIPHERED_LABEL = ''
            line_number = 0
            for line in reader.readlines():
                line_number += 1
                ENCIPHERED_LABEL = ENCIPHERED_LABEL + ' ' + str(line_number) + SPACES + line + '\n'
        print('>>> ' + CIPHERTEXT_TXT_NAME + ' [read]')
    except IOError:
        if not os.access(WORK_DIRECTORY + CIPHERTEXT_TXT_NAME, os.F_OK):
            new_enciphered_txt = open(WORK_DIRECTORY + CIPHERTEXT_TXT_NAME, 'w', encoding = ENCODING_MODE)
            new_enciphered_txt.close()
            print('>>> ' + CIPHERTEXT_TXT_NAME + ' [made]')
        temp = ''
        line_number = 0
        for line in ENCIPHERED_LABEL.splitlines(True):
            line_number += 1
            temp = temp + ' ' + str(line_number) + SPACES + line + '\n'
        ENCIPHERED_LABEL = temp
    print('>>> ' + 'ENCIPHERED_LABEL:')
    print(ENCIPHERED_LABEL)


def count():
    letter_numbers = \
        {'all': 0,
         'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
         'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in ENCIPHERED_LABEL:
        if letter.isupper():
            letter_numbers[letter] += 1
            letter_numbers['all'] += 1
    print('>>> ' + 'letter_numbers:')
    print(str(letter_numbers))
    return letter_numbers


def explorer():
    check_dir()
    os.startfile(WORK_DIRECTORY, EXPLORER_MODE)
    print('>>> ' + WORK_DIRECTORY + ' [' + EXPLORER_MODE + '(ed)]')


def decipher(boxes):
    cipher = {}
    for letter in UPPER_ALPHABET[1:27]:
        cipher[letter] = boxes[letter].get()
    for number in range(0, 10):
        cipher[str(number)] = str(number)
    cipher[' '] = ' '
    cipher['\n'] = '\n'

    result = ''
    for letter in ENCIPHERED_LABEL:
        if letter in cipher:
            result = result + cipher[letter]
        else:
            print('\'' + letter + '\'')
    print('>>> ' + 'result:')
    print(result)
    return result


def save(text):
    check_dir()
    txt_name = time.strftime("%m%d-%H%M-%S") + '.txt'
    with open(WORK_DIRECTORY + txt_name, 'w', encoding = ENCODING_MODE) as writer:
        writer.write(text)
    print('>>> ' + txt_name + ' [saved]')
    return txt_name


# **********************************************************************************************************************


def launch():
    def explorer_command():
        print('[explorer_command]:')
        explorer()
        print()

    def decipher_command():
        print('[decipher_command]:')
        root_fa.title('*' + PROJECT_TITLE)
        result_var.set(DEFAULT_RESULT)
        root_fa.update()
        time.sleep(0.3)
        result_var.set(decipher(boxes))
        print()

    def save_command():
        print('[save_command]:')
        root_fa.title(PROJECT_TITLE + ' • ' + save(result_var.get()) + ' [saved]')
        root_fa.update()
        print()

    # ------------------------------------------------------------------------------------------------------
    # read() & count()
    print('--------------------------------------------------------------------------------------')
    print(PROJECT_TITLE + ' by ' + AUTHOR_NAME)
    print('--------------------------------------------------------------------------------------')
    read()
    letter_numbers = count()
    print('--------------------------------------------------------------------------------------')
    print(' ||')

    # set fa
    root_fa = Tk()
    root_fa.geometry('1300x600+130+60')
    root_fa.title('*' + PROJECT_TITLE)
    root_fa.resizable(width = False, height = False)

    # set fb
    left_fb = Frame(root_fa, width = 300, height = 600,
                    highlightthickness = 1,
                    highlightbackground = 'grey')
    left_fb.grid(row = 0, column = 1)
    left_fb.grid_propagate(False)
    right_fb = Frame(root_fa, width = 1000, height = 600,
                     highlightthickness = 1,
                     highlightbackground = 'grey')
    right_fb.grid(row = 0, column = 2)
    right_fb.grid_propagate(False)

    # set fc
    left0_fc = Frame(left_fb, width = 300, height = 10)
    left0_fc.grid(row = 0, column = 0)
    left0_fc.grid_propagate(False)
    left1_fc = Frame(left_fb, width = 300, height = 490)
    left1_fc.grid(row = 1, column = 0)
    left1_fc.grid_propagate(False)
    left2_fc = Frame(left_fb, width = 300, height = 100)
    left2_fc.grid(row = 2, column = 0)
    left2_fc.grid_propagate(False)
    right1_fc = Frame(right_fb, width = 1000, height = 300)
    right1_fc.grid(row = 1, column = 0)
    right1_fc.grid_propagate(False)
    right2_fc = Frame(right_fb, width = 1000, height = 300)
    right2_fc.grid(row = 2, column = 0)
    right2_fc.grid_propagate(False)

    # set fd
    blank1_fd = Frame(left1_fc, width = 22, height = 500)
    blank1_fd.grid(row = 0, column = 1)
    blank1_fd.grid_propagate(False)
    am_fd = Frame(left1_fc, width = 128, height = 500)
    am_fd.grid(row = 0, column = 2)
    am_fd.grid_propagate(False)
    blank2_fd = Frame(left1_fc, width = 5, height = 500)
    blank2_fd.grid(row = 0, column = 3)
    blank2_fd.grid_propagate(False)
    nz_fd = Frame(left1_fc, width = 145, height = 500)
    nz_fd.grid(row = 0, column = 4)
    nz_fd.grid_propagate(False)

    # set result_var
    result_var = StringVar()
    result_var.set(DEFAULT_RESULT)

    # left1_fc
    boxes = {}
    fds = \
        (am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd, am_fd,
         nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd, nz_fd)
    for i in range(1, 27):
        percent = round((letter_numbers[UPPER_ALPHABET[i]] / letter_numbers['all']) * 100, 2)
        Label(fds[i - 1], text = str(percent) + '%', font = ('microsoft yahei', 11)) \
            .grid(row = i, column = 1, ipadx = 0, ipady = 0)
        Label(fds[i - 1], text = UPPER_ALPHABET[i], font = ('microsoft yahei', 12)) \
            .grid(row = i, column = 2, ipadx = 0, ipady = 5)
        box = Spinbox(fds[i - 1], values = LOWER_ALPHABET, font = 0, wrap = True, justify = CENTER, width = 1)
        box.grid(row = i, column = 3, ipadx = 6, ipady = 2)
        boxes[UPPER_ALPHABET[i]] = box

    # left2_fc
    Button(left2_fc, command = explorer_command, text = 'open directory', font = ('Times', 12, 'bold')) \
        .grid(row = 1, column = 1, padx = 90, pady = 2, ipadx = 4, ipady = 1)
    Button(left2_fc, command = decipher_command, text = 'DECIPHER', font = ('Times', 13, 'bold')) \
        .grid(row = 2, column = 1, padx = 0, pady = 12, ipadx = 2, ipady = 1)

    # right1_fc
    Label(right1_fc, text = ENCIPHERED_LABEL, font = ('microsoft yahei', 12), justify = LEFT) \
        .grid(row = 0, column = 0, padx = 36, pady = 12)

    # right2_fc
    Button(right2_fc, command = save_command, text = 'S\nA\nV\nE', font = ('Times', 13, 'bold')) \
        .grid(row = 0, column = 1, padx = 15, pady = 0, ipadx = 1, ipady = 9)
    Label(right2_fc, textvariable = result_var, font = ('microsoft yahei', 12), justify = LEFT, anchor = 'nw',
          highlightthickness = 1, highlightbackground = 'grey', bg = 'white', width = 69, height = 13) \
        .grid(row = 0, column = 2, padx = 0, pady = 7)
    Label(right2_fc, text = AUTHOR_LABEL, font = ('microsoft yahei', 13), justify = LEFT) \
        .grid(row = 0, column = 3, padx = 13, pady = 0)

    root_fa.mainloop()


# **********************************************************************************************************************


if __name__ == '__main__':
    launch()
