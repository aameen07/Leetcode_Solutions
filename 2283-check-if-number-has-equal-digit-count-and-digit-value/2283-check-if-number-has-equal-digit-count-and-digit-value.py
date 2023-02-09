class Solution:
    def digitCount(self, num: str) -> bool:
        
        
        d={}
        # d=collections.defaultdict(int)
        
        for i in num:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for j in range(len(num)):
            
            if d.get(str(j),0) != int(num[j]):
                return False
        return True
        
        
        