class DLinkedList():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU cache can be implemented using default orderedDict from collections in python. One another method is using hashmap and doublelinked list.
    """
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DLinkedList(),DLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node_head(self, node):
        # Add node at the start of the head
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        # Remove a node 
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node_head(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    # @return an integer
    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        else:
            self._move_to_head(node)
            return node.value
    
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = self.cache.get(key)
        
        if not node:
            new_node = DLinkedList()
            new_node.key = key
            new_node.value = value

            self.cache[key] = new_node
            self._add_node_head(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                tail_pop = self._pop_tail()
                del self.cache[tail_pop.key]
                self.size -= 1
        
        else:
            node.value = value
            self._move_to_head(node)
    
    def __str__(self):
        node = self.head.next
        r = []
        while(node):
            r.append(node.value)
            node = node.next
        return ' -> '.join(list(map(str,r)))
    
    def __repr__(self):
        node = self.head.next
        r = []
        while(node):
            r.append(node.value)
            node = node.next
        return ' -> '.join(list(map(str,r)))


x = LRUCache(3)
x.set(5,3)
x.set(4,2)
print(x.__str__())
print(x.get(4))
print(x)
x.set(4,3)
print(x.get(4))
x.set(2,5)
print(x)
x.set(8,9)
print(x)
print(x.get(5))