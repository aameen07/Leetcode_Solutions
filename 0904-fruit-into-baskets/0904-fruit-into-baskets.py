class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = collections.defaultdict(int)
        l,res = 0,0
        for r,i in enumerate(fruits):     # her r is index position and i is the element of fruit array
            if i in d:
                d[i]+=1
            else:
                d[i]=1  
            
            
            while(len(d)>2):
                f=fruits[l]
                d[f]-=1
                l+=1
                if d[f]==0:
                    d.pop(f) 
                    
            res = max(res, r-l+1)
        
        return res