class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        count=0
        
        for char in t:
            if count<len(s) and s[count]==char:
                count+=1
        
        return len(s)==count
    
# Humne ye check kia ke kys s string t string mei seq mei hai available uske liye s ki length check ki everytime and also ye check kia ke wo kya seq mei mil rha hai ya nhi 
# and end mei check kia ke kya saare characters s ke t mei the ya nhi seq mei tbhi un dono ka count same aaega