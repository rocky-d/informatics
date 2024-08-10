from collections import deque
from copy import copy
from typing import List, Set


def main() -> None:
    n, q = map(int, input().split())
    fields = input().split()
    statements = (input() for _ in range(q))

    statements = list(statements)
    fields_dct = {field: idx for idx, field in enumerate(fields)}
    db_lst = None
    db = []

    def insert(values: List[str]) -> None:
        db.append(values)

    def select(target: str, field: str, value: str) -> List[str]:
        res = list()
        target = fields_dct[target]
        field = fields_dct[field]
        for idx, row in enumerate(db):
            if value == row[field]:
                res.append(row[target])
        return res

    def _select_in(target: str, field: str, values: Set[str]) -> Set[str]:
        res = set()
        target = fields_dct[target]
        field = fields_dct[field]
        for idx, row in enumerate(db):
            if row[field] in values:
                res.add(row[target])
        return res

    def select_in(target: str, field: str, values: Set[str]) -> List[str]:
        res = list()
        target = fields_dct[target]
        field = fields_dct[field]
        for idx, row in enumerate(db):
            if row[field] in values:
                res.append(row[target])
        return res

    def delete(field: str, value: str) -> int:
        res = []
        field = fields_dct[field]
        for idx, row in enumerate(db):
            if value == row[field]:
                res.append(idx)
        for idx in reversed(res):
            del db[idx]
        return len(res)

    def delete_in(field: str, values: Set[str]) -> int:
        res = []
        field = fields_dct[field]
        for idx, row in enumerate(db):
            if row[field] in values:
                res.append(idx)
        for idx in reversed(res):
            del db[idx]
        return len(res)

    for i, statement in enumerate(statements):
        if 'begin()' == statement:
            for j in range(i + 1, q):
                if 'c' == statements[j][0]:
                    break
                elif 'a' == statements[j][0]:
                    db_lst = db
                    db = copy(db_lst)
                    break
        elif 'commit()' == statement:
            pass
        elif 'abort()' == statement:
            db = db_lst
        else:
            if 'insert(' == statement[:7]:
                insert(statement[7:-1].split(','))
            elif 'select(' == statement[:7]:
                target, field, value = statement[7:-1].split(',')
                res = select(target, field, value)
                print(len(res))
                if 0 < len(res):
                    print(res[0])
                    print(res[(len(res) - 1) // 2])
                    print(res[-1])
            elif 'delete(' == statement[:7]:
                field, value = statement[7:-1].split(',')
                res = delete(field, value)
                print(res)
            elif 'select_in(' == statement[:10]:
                stk = deque([''])
                for char in statement:
                    if '(' == char:
                        stk.append('')
                    elif ')' == char:
                        break
                    else:
                        stk[-1] += char
                target, field, value = stk.pop().split(',')
                res = set(select(target, field, value))
                while 2 < len(stk):
                    target, field, _ = stk.pop().split(',')
                    res = _select_in(target, field, res)
                target, field, _ = stk.pop().split(',')
                res = select_in(target, field, res)
                print(len(res))
                if 0 < len(res):
                    print(res[0])
                    print(res[(len(res) - 1) // 2])
                    print(res[-1])
            elif 'delete_in(' == statement[:10]:
                stk = deque([''])
                for char in statement:
                    if '(' == char:
                        stk.append('')
                    elif ')' == char:
                        break
                    else:
                        stk[-1] += char
                target, field, value = stk.pop().split(',')
                res = set(select(target, field, value))
                while 2 < len(stk):
                    target, field, _ = stk.pop().split(',')
                    res = _select_in(target, field, res)
                field, _ = stk.pop().split(',')
                res = delete_in(field, res)
                print(res)


if __name__ == '__main__':
    main()
