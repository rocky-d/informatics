class Grammar(object):

    def __init__(self) -> None:
        self.start: str = str()
        self.g_list: list[tuple[str, str]] = list()
        self.g_dict: dict[str, list[str]] = dict()
        self.vns: set[str] = set()
        self.vts: set[str] = set()
        self.phrases: set[str] = set()
        self.firstvt: dict[str, set[str]] = dict()
        self.lastvt: dict[str, set[str]] = dict()
        self.priorities: dict[str, dict[str, str]] = dict()

    def get_grammar(self) -> None:
        print('请输入“N::=aBcDe”形式的规则：')
        while True:
            string = input()
            if '' == string and 0 < len(self.g_list):
                break
            else:
                rule_tuple = tuple(string.split('::=', 1))
                if 1 < len(rule_tuple) and 1 == len(rule_tuple[0]) and rule_tuple[0][0].isupper():
                    self.g_list.append((rule_tuple[0], rule_tuple[1]))
                    if rule_tuple[0] not in self.g_dict.keys():
                        self.g_dict[rule_tuple[0]] = []
                    self.g_dict[rule_tuple[0]].append(rule_tuple[1])
                else:
                    print('\033[31m' + '无效规则！' + '\033[0m')
                    print('请输入“N::=aBcDe”形式的规则：')
        self.start, start_word = 'z', f"#{self.g_list[0][0]}#"
        self.g_list.insert(0, (self.start, start_word))
        self.g_dict[self.start] = [start_word]
        print(f"{self.start = }")
        print(f"{self.g_list = }")
        print(f"{self.g_dict = }")

    def get_vns_vts(self) -> None:
        for rule in self.g_list:
            self.vns |= set(rule[0])
            self.vts |= set(rule[1])
        self.vts |= set('#')
        self.vts -= self.vns
        print(f"{self.vns = }")
        print(f"{self.vts = }")

    def get_phrases(self) -> None:
        valid = True
        problems = []
        for rule in self.g_list:
            last_vn = False
            for char in rule[1]:
                if char in self.vns:
                    if last_vn:
                        valid = False
                        problems.append(f"{rule[0]}::={rule[1]}")
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
            raise Exception()

        for rule in self.g_list:
            phrase = ''
            for char in rule[1]:
                phrase += char if char in self.vts else 'N'
            self.phrases.add(phrase)
        print(f"{self.phrases = }")

    def get_firstvt_lastvt(self) -> None:
        def find_firstvt(vn_: str) -> None:
            self.firstvt[vn_] = set()
            for word_ in self.g_dict[vn_]:
                if 0 == len(word_):
                    raise Exception()
                elif 1 == len(word_):
                    if word_[0] in self.vts:
                        self.firstvt[vn_] |= set(word_[0])
                    else:
                        if word_[0] not in self.firstvt.keys():
                            find_firstvt(word_[0])
                        self.firstvt[vn_] |= self.firstvt[word_[0]]
                else:  # elif 2 <= len(word_):
                    if word_[0] in self.vts:
                        self.firstvt[vn_] |= set(word_[0])
                    else:
                        if word_[0] not in self.firstvt.keys():
                            find_firstvt(word_[0])
                        self.firstvt[vn_] |= self.firstvt[word_[0]] | set(word_[1])

        def find_lastvt(vn_: str) -> None:
            self.lastvt[vn_] = set()
            for word_ in self.g_dict[vn_]:
                if 0 == len(word_):
                    raise Exception()
                elif 1 == len(word_):
                    if word_[-1] in self.vts:
                        self.lastvt[vn_] |= set(word_[-1])
                    else:
                        if word_[-1] not in self.lastvt.keys():
                            find_lastvt(word_[-1])
                        self.lastvt[vn_] |= self.lastvt[word_[-1]]
                else:  # elif 2 <= len(word_):
                    if word_[-1] in self.vts:
                        self.lastvt[vn_] |= set(word_[-1])
                    else:
                        if word_[-1] not in self.lastvt.keys():
                            find_lastvt(word_[-1])
                        self.lastvt[vn_] |= self.lastvt[word_[-1]] | set(word_[-2])

        for vn in self.vns:
            if vn not in self.firstvt.keys():
                find_firstvt(vn)
            if vn not in self.lastvt.keys():
                find_lastvt(vn)
        print(f"{self.firstvt = }")
        print(f"{self.lastvt = }")

    def get_priorities(self) -> None:
        self.priorities = {vt: {vt: '/' for vt in self.vts} for vt in self.vts}
        for rule in self.g_list:
            word = rule[1]
            for i, char in enumerate(word):
                if char in self.vns:
                    continue
                if 1 < i:
                    former_former = word[i - 2]
                    if former_former in self.vts:
                        if self.priorities[former_former][char] == '/':
                            self.priorities[former_former][char] = '='
                        elif self.priorities[former_former][char] != '=':
                            print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                            raise Exception()
                if len(word) - 2 > i:
                    latter_latter = word[i + 2]
                    if latter_latter in self.vts:
                        if self.priorities[char][latter_latter] == '/':
                            self.priorities[char][latter_latter] = '='
                        elif self.priorities[char][latter_latter] != '=':
                            print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                            raise Exception()
                if 0 < i:
                    former = word[i - 1]
                    if former in self.vts:
                        if self.priorities[former][char] == '/':
                            self.priorities[former][char] = '='
                        elif self.priorities[former][char] != '=':
                            print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                            raise Exception()
                    else:
                        for lastvt_former in self.lastvt[former]:
                            if self.priorities[lastvt_former][char] == '/':
                                self.priorities[lastvt_former][char] = '>'
                            elif self.priorities[lastvt_former][char] != '>':
                                print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                                raise Exception()
                if len(word) - 1 > i:
                    latter = word[i + 1]
                    if latter in self.vts:
                        if self.priorities[char][latter] == '/':
                            self.priorities[char][latter] = '='
                        elif self.priorities[char][latter] != '=':
                            print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                            raise Exception()
                    else:
                        for firstvt_latter in self.firstvt[latter]:
                            if self.priorities[char][firstvt_latter] == '/':
                                self.priorities[char][firstvt_latter] = '<'
                            elif self.priorities[char][firstvt_latter] != '<':
                                print('\033[31m' + '该文法不是算符优先文法！' + '\033[0m')
                                raise Exception()
        print('\033[32m' + '该文法是算符优先文法。' + '\033[0m')

        print('self.priorities:')
        vt_order = sorted(self.vts, reverse = True)
        print('\t ', *vt_order, sep = '  ')
        for left in vt_order:
            print(f"\t{left}", end = '')
            for right in vt_order:
                relation = self.priorities[left][right]
                if relation == '/':
                    print(f"   ", end = '')
                else:
                    print(f"  {relation}", end = '')
            print()

    def analyse(self) -> None:
        print('请输入需要分析的符号串：')
        string_ = '^'
        while '$' != string_[-1]:
            string_ += input()
        string_ = string_[1:-1]
        string_ = string_.replace('while', 'w')
        string_ = string_.replace('if', 'f')
        string_ = string_.replace('else', 'e')
        string_ = string_.replace('==', '_')
        string_ = string_.replace('>=', '>_')
        string_ = string_.replace('<=', '<_')
        new_string = ''
        for char in string_:
            if not char.isspace():
                new_string += char
        string_ = new_string
        print('移入/归约过程如下：')
        print(f"\t{'stack   ':^30}{'      string':^60}  移入/归约 ?")
        try:
            string = list(f"#{string_}#")
            stack1 = [string.pop(0)]
            stack2, t_num = [], 0
            stack3 = []
            stack4 = []
            stack5 = []
            row = 0
            buffer2 = []
            while '#N#' != ''.join(stack1):
                buffer1 = '\t'
                buffer1 += f"{''.join(stack1):<30}"
                buffer1 += f"{''.join(string):>60}"
                if stack1[-1] in self.vts:
                    priority = self.priorities[stack1[-1]][string[0]]
                    min_pop_times = 1
                else:
                    priority = self.priorities[stack1[-2]][string[0]]
                    min_pop_times = 2
                if '<' == priority or '=' == priority:
                    stack1.append(string.pop(0))
                    buffer1 += f"    移入 {stack1[-1]:^5}"

                    if 'f' == stack1[-1]:
                        stack4.append(-1)
                        stack5.append('f')
                    elif 'e' == stack1[-1]:
                        stack4.append(-1)
                        stack5.append('e')
                    elif 'w' == stack1[-1]:
                        stack4.append(row + 1)
                        stack5.append('w')
                    elif '}' == stack1[-1]:
                        match stack5.pop(-1):
                            case 'f':
                                stack3.append(row + 1)
                            case 'w':
                                stack3.append(row + 2)
                        goto = stack4.pop(-1)
                        if -1 != goto:
                            row += 1
                            buffer2.append(f"\t{row:>3}. ( {'RJ':>4}, {goto:>4}, {'':>4}, {'':>4})")
                elif '>' == priority:
                    phrase = ''
                    for _ in range(min_pop_times):
                        phrase = stack1.pop(-1) + phrase
                    while phrase not in self.phrases:
                        phrase = stack1.pop(-1) + phrase
                    stack1.append('N')
                    buffer1 += f"    归约 {phrase:^5}"

                    if '=N' == phrase[-2:]:
                        row += 1
                        to = phrase[:-2]
                        buffer2.append(f"\t{row:>3}. ( {'=':>4}, {stack2.pop(-1):>4}, {'':>4}, {to:>4})")
                    elif phrase in ('N_N', 'N>N', 'N>_N', 'N<N', 'N<_N'):
                        row += 1
                        t_num += 1
                        to = f"t{t_num}"
                        buffer2.append(f"\t{row:>3}. ( {phrase[1:-1]:>4}, {stack2.pop(-2):>4}, {stack2.pop(-1):>4}, {to:>4})")
                        stack2.append(f"t{t_num}")
                        row += 1
                        buffer2.append(f"\t{row:>3}. ( {'FJ':>4}, [], {stack2.pop(-1):>4}, {'':>4})")
                    elif phrase in ('N+N', 'N-N', 'N*N', 'N/N'):
                        row += 1
                        t_num += 1
                        to = f"t{t_num}"
                        buffer2.append(f"\t{row:>3}. ( {phrase[1]:>4}, {stack2.pop(-2):>4}, {stack2.pop(-1):>4}, {to:>4})")
                        stack2.append(f"t{t_num}")
                    elif 'i' == phrase:
                        row += 1
                        t_num += 1
                        to = f"t{t_num}"
                        buffer2.append(f"\t{row:>3}. ( {'=':>4}, {'i':>4}, {'':>4}, {to:>4})")
                        stack2.append(f"t{t_num}")
                else:  # elif '/' == priority:
                    print('\033[31m' + '符号串存在语法错误！' + '\033[0m')
                    break
                print(buffer1)
            else:
                buffer1 = '\t'
                buffer1 += f"{''.join(stack1):<30}"
                buffer1 += f"{''.join(string):>60}"
                buffer1 += f"    归约 {'#N#':^5}"
                print(buffer1)
                print('\033[32m' + '分析完毕，符号串正确。' + '\033[0m')

                row += 1
                buffer2.append(f"\t{row:>3}. ( {'':>4}, {'':>4}, {'':>4}, {'':>4})")

                buffer3 = '\n'.join(buffer2)
                while 0 < len(stack3):
                    buffer3 = buffer3.replace('[]', f"{stack3.pop(-1):>4}", 1)
                print(buffer3)
        except IndexError:
            print('\033[31m' + '符号串存在语法错误！' + '\033[0m')
        except KeyError:
            print('\033[31m' + '符号串存在词法错误！' + '\033[0m')


if __name__ == '__main__':
    grammar = Grammar()
    grammar.get_grammar()
    grammar.get_vns_vts()
    grammar.get_phrases()
    grammar.get_firstvt_lastvt()
    grammar.get_priorities()
    while True:
        grammar.analyse()

'''
X::=W
X::=I
X::=V
W::=wC{V}
I::=fC{V}e{V}
I::=fC{V}
C::=(B)
B::=E_E
B::=E>E
B::=E>_E
B::=E<E
B::=E<_E
V::=D;
D::=D;S
D::=S
S::=a=E
S::=b=E
S::=c=E
S::=d=E
S::=x=E
S::=y=E
E::=E+T
E::=E-T
E::=T
T::=T*F
T::=T/F
T::=F
F::=(E)
F::=i
'''
'''
if (i*i > i+i/(i*i)) {
    x = (i+i)*i;
} else {
    a = i-i/(i+i);
    b = i;
}$
'''
'''
while (i <= i+i/(i*i)) {
    a = i-i/(i+i);
    b = i;
}$
'''
