class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cursize = 0
        self.minfreq = 0
        self.cache = {}
        self.freqmap = {}

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self.update(node)
        else:
            self.cursize += 1
            if self.cursize > self.cap:
                list = self.freqmap.get(self.minfreq)
                del self.cache[list.tail.prev.key]
                list.removeNode(list.tail.prev)
                self.cursize -= 1
            self.minfreq = 1
            newnode = ListNode(key, value)
            curlist = self.freqmap.get(1, DLL())
            curlist.insertNode(newnode)
            self.freqmap[1] = curlist
            self.cache[key] = newnode
        
    def update(self, node: ListNode) -> None:
        freq = node.freq
        list = self.freqmap.get(freq)
        list.removeNode(node)
        if freq == self.minfreq and list.size == 0:
            self.minfreq += 1
        node.freq += 1
        newlist = self.freqmap.get(node.freq, DLL())
        newlist.insertNode(node)
        self.freqmap[node.freq] = newlist

class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertNode(self, node: ListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def removeNode(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    # def update(node):
    #     curfreq = node.freq
    #     list = freqmap[curfreq]
    #     list.removeNode(node)
    #     if curfreq == minfreq and list.listSize == 0:
    #         minfreq += 1
    #     node.freq += 1
    #     newlist = freqmap.get(node.freq, DLL())
    #     newlist.insertNode(node)
    #     freqmap[node.freq] = newlist


# class LFUCache:    
    
#     def __init__(self, capacity: int):
#         self.cap=capacity
#         self.curSize=0
#         self.minFreq=0
        
#         self.cacheDic={}
#         self.freqDic={}
        

#     def get(self, key: int) -> int:
#         curNode=self.cacheDic.get(key)
#         if not curNode:
#             return -1
#         self.updateNode(curNode)
#         return curNode.val

#     def put(self, key: int, value: int) -> None:
#         if self.cap==0:
#             return -1   #check again
        
#         if key in self.cacheDic:
#             curNode=self.cacheDic.get(key)
#             curNode.val=value
#             self.updateNode(curNode)
        
#         else:
#             self.curSize+=1
            
#             if self.curSize>self.cap:
#                 minFreqList=self.freqDic.get(self.minFreq)
#                 self.cacheDic.remove(minFreqList.tail.prev.key)
#                 minFreqList.removeNode(minFreqList.tail.prev)
#                 curSize-=1
            
#             minFreq=1
#             newNode=DLLNode(key,value)
#             curList=self.freqDic.get(1, DoubleLinkedList())
#             curList.addNode(newNode)
#             self.freqDic.put(1,curList)
#             self.cacheDic.put(key,newNode)


#     def updateNode(self, curNode):
#         curFreq=curNode.freq
#         curList=freqDic.get(curFreq)
#         curList.removeNode(curNode)
        
#         if curFreq==minFreq and len(curList) == 0:
#             minFreq+=1
        
#         curNode.freq+=1
        
#         newList=freqDic.get(curNode.freq, DoubleLinkedList())


# class DLLNode:
#     def __init__(self,key,value):
#         self.key=key
#         self.val=value
#         self.freq=1
#         self.prev=self.next=None


# class DoubleLinkedList:

#     def __init__(self,head=None,tail=None):
#         self.listSize=0
#         self.head=DLLNode(0,0)
#         self.tail=DLLNode(0,0)
#         self.head.next=tail
#         self.tail.prev=head
    
#     def addNode(self,curNode):
#         nextNode=self.head.next
#         curNode.next=nextNode
#         curNode.prev=self.head
#         self.head.next=curNode
#         nextNode.prev=curNode
#         self.listSize+=1
        
#     def removeNode(self,curNode):
#         prevNode=curNode.prev
#         nextNode=curNode.next
#         prevNode.next=nextNode
#         nextNode.prev=prevNode
#         self.listSize-=1
        
        
        
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)