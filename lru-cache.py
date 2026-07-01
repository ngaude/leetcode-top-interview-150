class ListNode:
    def __init__(self, val=0, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = next
        self.key = None
    
    def __str__(self):
        curr = self
        s = []
        while curr and len(s) < 100:
            s.append(str(curr.val))
            curr = curr.next
        return '->'.join(s)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-77)
        self.tail = ListNode(99)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
    
    def __detach(self, n: ListNode):
        # detach
        n.prev.next = n.next
        n.next.prev = n.prev
        n.next = None
        n.prev = None
        

    def __push(self, n: ListNode):
        # insert @ tail
        nn = self.tail.prev
        nn.next = n
        n.prev = nn
        n.next = self.tail
        self.tail.prev = n
    
    def __use(self, n: ListNode):
        self.__detach(n)
        self.__push(n)

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.__use(n)
            return n.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
            
        if key in self.cache:
            n = self.cache[key]
            n.val = value
            self.__use(n)
        else:
            while len(self.cache) >= self.capacity:
                lru = self.head.next
                self.__detach(lru)
                self.cache.pop(lru.key)

            n = ListNode(value)
            n.key = key
            self.__push(n)
            self.cache[key] = n
        



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
assert lRUCache.get(1) == 1   # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
assert lRUCache.get(2) == -1    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
assert lRUCache.get(1) == -1   # return -1 (not found)
assert lRUCache.get(3) == 3    # return 3
assert lRUCache.get(4) == 4   # return 4