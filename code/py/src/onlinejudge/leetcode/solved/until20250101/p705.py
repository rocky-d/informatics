class MyHashSet:
    def __init__(self) -> None:
        self.vals = [False for _ in range(1_000_001)]

    def add(self, key: int) -> None:
        self.vals[key] = True

    def remove(self, key: int) -> None:
        self.vals[key] = False

    def contains(self, key: int) -> bool:
        return self.vals[key]
