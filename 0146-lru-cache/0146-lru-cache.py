class Node:         # this class is for creating new Node
    def __init__(self,key,value):
        self.key,self.val=key,value
        self.prev=self.next=None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.d={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if key in self.d:
            n=self.d[key]
            self.remove(self.d[key])
            self.insert(n)
            return n.val
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        elif len(self.d) == self.cap:
            self.remove(self.tail.prev)
        self.insert(Node(key,value))
        
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        del self.d[node.key]     #we're deleting the entry from dic by taking key from the node
        
    def insert(self,node):
        self.d[node.key]=node
        right=self.head.next
        left=self.head
        
        left.next=right.prev=node
        node.prev=left
        node.next=right
        
        
            # or
            
            
            
# class Node:
#     def __init__(self,key,val):
#         self.key,self.val=key,val
#         self.prev=self.next=None
        
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap=capacity
#         self.cache={}
#         #left=LRU, right=Most recent
#         self.left, self.right = Node(0,0), Node(0,0)
#         self.left.next, self.right.prev = self.right, self.left

#     def remove(self,node):
#         prev,nxt = node.prev, node.next
#         prev.next,nxt.prev = nxt,prev
        
#     def insert(self,node):
#         prev,nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev
        
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1
        
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key]=Node(key,value)
#         self.insert(self.cache[key])
        
#         if len(self.cache) > self.cap:
#             lru=self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)