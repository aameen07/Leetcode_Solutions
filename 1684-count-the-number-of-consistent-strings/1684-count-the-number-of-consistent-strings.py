class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        res=0
        
        for i in words:
            flag=True
            for j in i:
                if j not in allowed:
                    flag=False
            if flag:
                res+=1
        
        return res