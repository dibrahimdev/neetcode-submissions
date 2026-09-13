class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.used_size = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        slot = key % self.size
        for pair in self.used_size[slot]:
            if pair[0] == key:
                pair[1] = value
                return
        self.used_size[slot].append([key, value])
        

    def get(self, key: int) -> int:
        slot = key % self.size
        for pair in self.used_size[slot]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        slot = key % self.size
        for pair in self.used_size[slot]:
            if pair[0] == key:
                self.used_size[slot].remove(pair)
                return 
                

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)