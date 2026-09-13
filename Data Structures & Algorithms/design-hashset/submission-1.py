class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.used_size = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        slot = key % self.size
        if key not in self.used_size[slot]:
            self.used_size[slot].append(key)
                

    def remove(self, key: int) -> None:
        slot = key % self.size
        if key in self.used_size[slot]:
            self.used_size[slot].remove(key)
        

    def contains(self, key: int) -> bool:
        slot = key % self.size
        return key in self.used_size[slot]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)