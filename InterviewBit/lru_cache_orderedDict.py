from collections import OrderedDict
class LRUCache(OrderedDict):
    # lang: Python2
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

x = LRUCache(3)
x.set(5,3)
x.set(4,2)
print(x.get(4))
print(x)
x.set(4,3)
print(x.get(4))
x.set(2,5)
print(x)
x.set(8,9)
print(x)
print(x.get(5))