class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        d1={}
        d2={}
        
        a = set(i[0] for i in paths)
        for j in paths:
            if j[1] not in a:
                return j[1]
        