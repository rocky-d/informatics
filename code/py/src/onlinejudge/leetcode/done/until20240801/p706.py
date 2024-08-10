class MyHashMap:
    def __init__(self) -> None:
        self.vals = [-1 for _ in range(1_000_001)]

    def put(self, key: int, value: int) -> None:
        self.vals[key] = value

    def get(self, key: int) -> int:
        return self.vals[key]

    def remove(self, key: int) -> None:
        self.vals[key] = -1
