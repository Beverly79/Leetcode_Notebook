class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.order = []
        
    def get(self, key: int) -> int:
        if key in self.order: # update used order
            self.order.remove(key)
            self.order.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.order: # update
            self.dic[key] = value
            self.order.remove(key)
            self.order.append(key)
        # else not in the dic
        elif len(self.dic) < self.capacity: # still room to put a new key
            self.dic[key] = value
            self.order.append(key)
        else: # evict the least recent used key
            del self.dic[self.order[0]] # delete the first key from dic
            del self.order[0] # delete the first key from order list
            
            self.dic[key] = value
            self.order.append(key)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)