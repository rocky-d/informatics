def lexical_analyzer(source: str) -> list[tuple[str, str]]:
    tokens = []
    keywords = [
        'switch', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'while',
        'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short',
        'signed', 'sizeof', 'static', 'struct', 'typedef', 'union', 'unsigned', 'void', 'printf', 'scanf',
    ]
    separators = [';', '(', ')', '{', '}', ',', '[', ']', '<', '>']
    operators = ['&', '+', '-', '*', '/', '=', '>', '<', '>=', '<=', '==', '!=', '++', '--', '+=', '-=', '*=', '/=',
                 '%=']

    # 排除注释
    # source = re.sub(r'//.*|/\*.*\*/', '', source)

    i = 0
    while i < len(source):
        if source[i].isspace():
            i += 1
        # 匹配分隔符
        elif source[i] in separators:
            tokens.append(('分隔符', source[i]))
            i += 1
        # 匹配注释
        elif source[i] == '/':
            comment = source[i]
            i += 1
            if source[i] == '/':
                while i < len(source) and source[i] != '\n':
                    comment += source[i]
                    i += 1
                i += 1
            elif source[i] == '*':
                while i < len(source) and source[i - 1:i + 1] != '*/':
                    comment += source[i]
                    i += 1
                comment += source[i]
                i += 1
            tokens.append(('注释', comment))
        # 匹配关键字或标识符
        elif source[i].isalpha() or source[i] == '_':
            identifier = source[i]
            i += 1
            while i < len(source) and (source[i].isalnum() or source[i] == '_'):
                identifier += source[i]
                i += 1
            tokens.append(('关键字' if identifier in keywords else '标识符', identifier))
        # 匹配数字常量
        elif source[i].isdigit():
            number = source[i]
            i += 1
            while i < len(source) and source[i].isdigit():
                number += source[i]
                i += 1
            tokens.append(('数字常量', number))
        # 匹配字符串常量
        elif source[i] == '"':
            string = ''
            i += 1
            while i < len(source) and source[i] != '"':
                string += source[i]
                i += 1
            tokens.append(('字符串常量', string))
            i += 1
        # 匹配运算符
        elif source[i] in operators:
            operator = source[i]
            i += 1
            if i < len(source) and source[i] in operators:
                operator += source[i]
                i += 1
            tokens.append(('运算符', operator))
        else:
            print(f'无法识别索引为{i}的字符，\'{source[i]}\'')
            i += 1
    print()
    return tokens


if __name__ == '__main__':
    dict_ = {'注释': [], '关键字': [], '标识符': [], '数字常量': [], '字符串常量': [], '分隔符': [], '运算符': []}
    with open(file = 'source.c', mode = 'r+', encoding = 'UTF_8') as f:
        for pair in lexical_analyzer(f.read()):
            print(pair)
            dict_[pair[0]].append(pair[1])
    # print()
    # for item in dict_.items():
    #     print(item[0] + ':')
    #     print(item[1])
