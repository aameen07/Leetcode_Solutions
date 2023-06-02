class ListNode:
    def __init__(self,key,val):
        self.pair=(key,val)
        self.next=None
    
class MyHashMap:
    def __init__(self):
        self.size=1000
        self.a=[None]*self.size
        
    def put(self, key: int, value: int) -> None:
        index=key%self.size
        if self.a[index]==None:
            self.a[index]=ListNode(key,value)
        else:
            pre=None
            cur=self.a[index]
            while (cur!=None):
                if cur.pair[0]==key:
                    cur.pair=(key,value)
                    return 
                pre=cur
                cur=cur.next
            pre.next=ListNode(key,value)

    def get(self, key: int) -> int:
        index=key%self.size
        if self.a[index]==None: return -1
        
        cur=self.a[index]
        while (cur!=None):
            if cur.pair[0]==key:
                return cur.pair[1]
            cur=cur.next
        
        return -1                

    def remove(self, key: int) -> None:
        index=key%self.size
        if self.a[index]==None: return 
        
        current=self.a[index]
        if current.pair[0]==key:
            self.a[index]=current.next
            return
        
        pre=None
        cur=self.a[index]
        while (cur!=None):
            if cur.pair[0]==key:
                pre.next=cur.next
                return
            pre=cur
            cur=cur.next
        return 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)