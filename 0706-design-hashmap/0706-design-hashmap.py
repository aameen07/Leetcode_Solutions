class ListNode:
    def __init__(self,key,val):
        self.pair=(key,val)
        self.next=None
    
class MyHashMap:

    def __init__(self):
        self.size=1000
        self.a=[None]*self.size

    def put(self, key: int, value: int) -> None:
        h=key%self.size
        if self.a[h]==None:
            self.a[h]=ListNode(key,value)
        else:
            pre=None
            cur=self.a[h]
            while (cur!=None):
                if cur.pair[0]==key:
                    cur.pair=(key,value)
                    return 
                pre=cur
                cur=cur.next
            
            pre.next=ListNode(key,value)
            

    def get(self, key: int) -> int:
        h=key%self.size
        if self.a[h]==None: return -1
        
        cur=self.a[h]
        while (cur!=None):
            if cur.pair[0]==key:
                return cur.pair[1]
            cur=cur.next
        
        return -1
                

    def remove(self, key: int) -> None:
        h=key%self.size
        if self.a[h]==None: return 
        
        
        curr=self.a[h]
        if curr.pair[0]==key:
            self.a[h]=curr.next
            return
        
        pre=None
        cur=self.a[h]
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