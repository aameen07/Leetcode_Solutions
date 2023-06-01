class MyHashSet:
    
    def __init__(self):
        self.size=1000
        self.a=[None]*self.size

    def add(self, key: int) -> None:
        h=key%self.size
        if not self.a[h]:
            self.a[h]=[key]
        elif key not in self.a[h]:
            self.a[h].append(key)
        
    def remove(self, key: int) -> None:
        h=key%self.size
        if self.a[h] and key in self.a[h]:
            self.a[h].remove(key)
            if len(self.a[h])==0:
                self.a[h]=None

    def contains(self, key: int) -> bool:
        h=key%self.size
        if self.a[h]:
            if key not in self.a[h]:
                return False
            else:
                return True
        else:
            return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)