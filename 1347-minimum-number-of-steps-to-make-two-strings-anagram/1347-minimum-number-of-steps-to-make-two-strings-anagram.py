class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in t:
            if j in dic and dic[j]>0:
                dic[j]-=1
        return sum(dic.values())
        
    # or
    
#         cs=collections.Counter(s)
#         ct=collections.Counter(t)
        
#         diff = cs-ct
#         return sum(diff.values())