def main() -> None:
    print('请输入“N::=aBcDe”形式的规则：')
    g_list, g_dict = [], {}
    while True:
        string_ = input()
        if '' == string_ and 0 < len(g_list):
            break
        else:
            rule_tuple = tuple(string_.split('::='))
            if 2 == len(rule_tuple) and 1 == len(rule_tuple[0]) and rule_tuple[0][0].isupper():
                g_list.append(rule_tuple)
                if rule_tuple[0] not in g_dict.keys():
                    g_dict[rule_tuple[0]] = []
                g_dict[rule_tuple[0]].append(rule_tuple[1])
            else:
                print('\033[31m' + '无效规则！' + '\033[0m')
                print('请输入“N::=aBcDe”形式的规则：')
    start, start_word = 'z', f'#{g_list[0][0]}#'
    g_list.insert(0, (start, start_word))
    g_dict[start] = [start_word]
    print(f'{start = }')
    print(f'{g_list = }')
    print(f'{g_dict = }')

    vn_set, vt_set = set(), set('#')
    for rule in g_list:
        vn_set |= set(rule[0])
        vt_set |= set(rule[1])
    vt_set -= vn_set
    print(f'{vn_set = }')
    print(f'{vt_set = }')

    valid = True
    problems = []
    for rule in g_list:
        last_vn = False
        for char in rule[1]:
            if char in vn_set:
                if last_vn:
                    valid = False
                    problems.append(f'{rule[0]}::={rule[1]}')
                    break
                else:
                    last_vn = True
            else:
                last_vn = False
    if valid:
        print('\033[32m' + '该文法是算符文法。' + '\033[0m')
    else:
        print('\033[31m' + '该文法不是算符文法！' + '\033[0m')
        print('请检查下列规则：')
        print('\n'.join(problems))
        return None

    phrases = set()
    for rule in g_list:
        phrase = ''
        for char in rule[1]:
            phrase += char if char in vt_set else 'N'
        phrases.add(phrase)
    print(f'{phrases = }')

    def find_firstvt(vn_: str) -> None:
        firstvt[vn_] = set()
        for word_ in g_dict[vn_]:
            if 0 == len(word_):
                ...  # TODO: 空串
            elif 1 == len(word_):
                if word_[0] in vt_set:
                    firstvt[vn_] |= set(word_[0])
                else:
                    if word_[0] not in firstvt.keys():
                        find_firstvt(word_[0])
                    firstvt[vn_] |= firstvt[word_[0]]
            else:
                if word_[0] in vt_set:
                    firstvt[vn_] |= set(word_[0])
                else:
                    if word_[0] not in firstvt.keys():
                        find_firstvt(word_[0])
                    firstvt[vn_] |= firstvt[word_[0]] | set(word_[1])

    def find_lastvt(vn_: str) -> None:
        lastvt[vn_] = set()
        for word_ in g_dict[vn_]:
            if 0 == len(word_):
                ...  # TODO: 空串
            elif 1 == len(word_):
                if word_[-1] in vt_set:
                    lastvt[vn_] |= set(word_[-1])
                else:
                    if word_[-1] not in lastvt.keys():
                        find_lastvt(word_[-1])
                    lastvt[vn_] |= lastvt[word_[-1]]
            else:
                if word_[-1] in vt_set:
                    lastvt[vn_] |= set(word_[-1])
                else:
                    if word_[-1] not in lastvt.keys():
                        find_lastvt(word_[-1])
                    lastvt[vn_] |= lastvt[word_[-1]] | set(word_[-2])

    firstvt, lastvt = {}, {}
    for vn in vn_set:
        if vn not in firstvt.keys():
            find_firstvt(vn)
        if vn not in lastvt.keys():
            find_lastvt(vn)
    print(f'{firstvt = }')
    print(f'{lastvt = }')

    priorities = {vt: {vt: '/' for vt in vt_set} for vt in vt_set}
    for rule in g_list:
        word = rule[1]
        for i, char in enumerate(word):
            if char in vn_set:
                continue
            if 1 < i:
                former_former = word[i - 2]
                if former_former in vt_set:
                    if priorities[former_former][char] == '/':
                        priorities[former_former][char] = '='
                    elif priorities[former_former][char] != '=':
                        print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                        return None
            if len(word) - 2 > i:
                latter_latter = word[i + 2]
                if latter_latter in vt_set:
                    if priorities[char][latter_latter] == '/':
                        priorities[char][latter_latter] = '='
                    elif priorities[char][latter_latter] != '=':
                        print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                        return None
            if 0 < i:
                former = word[i - 1]
                if former in vt_set:
                    if priorities[former][char] == '/':
                        priorities[former][char] = '='
                    elif priorities[former][char] != '=':
                        print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                        return None
                else:
                    for lastvt_former in lastvt[former]:
                        if priorities[lastvt_former][char] == '/':
                            priorities[lastvt_former][char] = '>'
                        elif priorities[lastvt_former][char] != '>':
                            print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                            return None
            if len(word) - 1 > i:
                latter = word[i + 1]
                if latter in vt_set:
                    if priorities[char][latter] == '/':
                        priorities[char][latter] = '='
                    elif priorities[char][latter] != '=':
                        print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                        return None
                else:
                    for firstvt_latter in firstvt[latter]:
                        if priorities[char][firstvt_latter] == '/':
                            priorities[char][firstvt_latter] = '<'
                        elif priorities[char][firstvt_latter] != '<':
                            print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                            return None
    print('\033[32m' + '该文法是算符优先文法。' + '\033[0m')

    print('priorities:')
    vt_order = sorted(vt_set, reverse = True)
    print('\t ', *vt_order, sep = '  ')
    for left in vt_order:
        print(f'\t{left}', end = '')
        for right in vt_order:
            relation = priorities[left][right]
            if relation == '/':
                print(f'   ', end = '')
            else:
                print(f'  {relation}', end = '')
        print()

    print()
    string_ = ''
    while 0 == len(string_):
        string_ = input('请输入需要分析的符号串：')
    print('移入/归约过程如下：')
    print(f"\t{'stack':^20}{'string':^40}  移入/归约 ?")
    try:
        string = list(f"#{string_}#")
        stack = [string.pop(0)]
        while '#N#' != ''.join(stack):
            buffer = '\t'
            buffer += f"{''.join(stack):<20}"
            buffer += f"{''.join(string):>40}"
            if stack[-1] in vt_set:
                priority = priorities[stack[-1]][string[0]]
                min_pop_times = 1
            else:
                priority = priorities[stack[-2]][string[0]]
                min_pop_times = 2
            if '<' == priority or '=' == priority:
                stack.append(string.pop(0))
                buffer += f'    移入 {stack[-1]:^5}'
            # elif '=' == priority:
            #     stack.append(string.pop(0))
            #     buffer += f'    移入 {stack[-1]:^5}'
            elif '>' == priority:
                phrase = ''
                for _ in range(min_pop_times):
                    phrase = stack.pop(-1) + phrase
                while phrase not in phrases:
                    phrase = stack.pop(-1) + phrase
                stack.append('N')
                buffer += f'    归约 {phrase:^5}'
            else:  # elif '/' == priority:
                print('\033[31m' + '符号串存在语法错误！' + '\033[0m')
                break
            print(buffer)
        else:
            print('\033[32m' + '分析完毕，符号串正确。' + '\033[0m')
    except KeyError:
        print('\033[31m' + '符号串存在词法错误！' + '\033[0m')
    except IndexError:
        print('\033[31m' + '符号串存在语法错误！' + '\033[0m')
    finally:
        print('程序结束。')


if __name__ == '__main__':
    main()

'''
E::=E+T
E::=T
T::=T*F
T::=F
F::=(E)
F::=i


i+i*i
i+(i+i)*i
i+(i+i*i+i*i*i+i)*(i+(i*i)*i)*i*i+i

'''
