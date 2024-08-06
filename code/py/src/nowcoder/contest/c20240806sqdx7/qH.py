from array import array
from collections import deque, defaultdict
from copy import copy, deepcopy
from typing import List, Set


def main() -> None:
    n, q = map(int, input().split())
    fields = input().split()
    statements = (input() for _ in range(q))

    fields_dct = {field: idx for idx, field in enumerate(fields)}
    db_lst = None
    db = deque()
    idxes_lst = None
    idxes = [defaultdict(lambda: array('I')) for _ in fields]
    deleted_lst = None
    deleted = set()

    def insert(values: List[str]) -> None:
        idx = len(db)
        db.append(values)
        for field, value in enumerate(values):
            idxes[field][value].append(idx)

    def select(target: str, field: str, value: str) -> List[str]:
        res = list()
        target = fields_dct[target]
        field = fields_dct[field]
        for idx in idxes[field][value]:
            if idx not in deleted:
                res.append(db[idx][target])
        return res

    def _select_in(target: str, field: str, values: Set[str]) -> Set[str]:
        res = set()
        target = fields_dct[target]
        field = fields_dct[field]
        for value in values:
            for idx in idxes[field][value]:
                if idx not in deleted:
                    res.add(db[idx][target])
        return res

    def select_in(target: str, field: str, values: Set[str]) -> List[str]:
        res = list()
        target = fields_dct[target]
        field = fields_dct[field]
        for value in values:
            for idx in idxes[field][value]:
                if idx not in deleted:
                    res.append(db[idx][target])
        return res

    def delete(field: str, value: str) -> int:
        res = 0
        field = fields_dct[field]
        for idx in idxes[field][value]:
            deleted.add(idx)
            res += 1
        return res

    def delete_in(field: str, values: Set[str]) -> int:
        res = 0
        field = fields_dct[field]
        for value in values:
            for idx in idxes[field][value]:
                deleted.add(idx)
                res += 1
        return res

    for statement in statements:
        if 'begin()' == statement:
            db_lst = db
            db = copy(db_lst)
            idxes_lst = idxes
            idxes = deepcopy(idxes_lst)
            deleted_lst = deleted
            deleted = copy(deleted_lst)
        elif 'commit()' == statement:
            pass
        elif 'abort()' == statement:
            db = db_lst
            idxes = idxes_lst
            deleted = deleted_lst
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
