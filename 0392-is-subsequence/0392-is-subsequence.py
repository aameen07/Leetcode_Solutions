class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        count=0
        
        for char in t:
            if count<len(s) and s[count]==char:
                count+=1
        
        return len(s)==count
    
# This checks if the 


        