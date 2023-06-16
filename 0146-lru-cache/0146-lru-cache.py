class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: node
        self.leastRecent = self.mostRecent = Node(0, 0)
        self.leastRecent.nxt, self.mostRecent.prev = self.mostRecent, self.leastRecent
        
    # remove node from list
    def remove(self, node):
        prevNode, nxtNode = node.prev, node.nxt
        prevNode.nxt, nxtNode.prev = nxtNode, prevNode
        
    # add node at right
    def insert(self, node):
        prev, nxt = self.mostRecent.prev, self.mostRecent
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        print(key in self.cache)
        if (key in self.cache):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
                

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove and delete the LRU from the cache/map
            lru = self.leastRecent.nxt
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)