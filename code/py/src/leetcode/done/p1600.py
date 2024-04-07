from rockyutil.leetcode import *


class ThroneInheritance:
    class Person(object):
        def __init__(self, name: str, children: List['ThroneInheritance.Person']) -> None:
            self.name = name
            self.children = children

    def __init__(self, kingName: str) -> None:
        king = ThroneInheritance.Person(name = kingName, children = [])
        self.king = king
        self.people = {kingName: king}

    def birth(self, parentName: str, childName: str) -> None:
        child = ThroneInheritance.Person(name = childName, children = [])
        self.people[parentName].children.append(child)
        self.people[childName] = child

    def death(self, name: str) -> None:
        del self.people[name]

    def getInheritanceOrder(self) -> List[str]:
        res = []

        def dfs(person: ThroneInheritance.Person) -> None:
            if person.name in self.people.keys():
                res.append(person.name)
            for child in person.children:
                dfs(child)

        dfs(person = self.king)
        return res
