from array import array
from collections import deque, defaultdict
from copy import copy, deepcopy
from typing import List, Set


def main() -> None:
    n, q = map(int, input().split())
    fields = input().split()

    fields_idxes = {field: idx for idx, field in enumerate(fields)}
    db_lst = None
    db = []
    idx_table_lst = None
    idx_table = [defaultdict(lambda: array('I')) for _ in range(n)]
    deleted_lst = None
    deleted = set()

    def insert(values: List[str]) -> None:
        idx = len(db)
        db.append(values)
        for field, value in enumerate(values):
            idx_table[field][value].append(idx)

    def select(target: str, field: str, value: str) -> List[str]:
        res = list()
        target = fields_idxes[target]
        field = fields_idxes[field]
        for idx in idx_table[field][value]:
            if idx not in deleted:
                res.append(db[idx][target])
        return res

    def _select_in(target: str, field: str, values: Set[str]) -> Set[str]:
        res = set()
        target = fields_idxes[target]
        field = fields_idxes[field]
        for value in values:
            for idx in idx_table[field][value]:
                if idx not in deleted:
                    res.add(db[idx][target])
        return res

    def select_in(target: str, field: str, values: Set[str]) -> List[str]:
        res = list()
        target = fields_idxes[target]
        field = fields_idxes[field]
        for value in values:
            for idx in idx_table[field][value]:
                if idx not in deleted:
                    res.append(db[idx][target])
        return res

    def delete(field: str, value: str) -> int:
        res = 0
        field = fields_idxes[field]
        for idx in idx_table[field][value]:
            deleted.add(idx)
            res += 1
        return res

    def delete_in(field: str, values: Set[str]) -> int:
        res = 0
        field = fields_idxes[field]
        for value in values:
            for idx in idx_table[field][value]:
                deleted.add(idx)
                res += 1
        return res

    for _ in range(q):
        statement = input()
        if 'begin()' == statement:
            db_lst = db
            db = copy(db_lst)
            idx_table_lst = idx_table
            idx_table = deepcopy(idx_table_lst)
            deleted_lst = deleted
            deleted = copy(deleted_lst)
        elif 'commit()' == statement:
            pass
        elif 'abort()' == statement:
            db = db_lst
            idx_table = idx_table_lst
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
