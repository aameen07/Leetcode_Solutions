class Solution:
    def reverseWords(self, s: str) -> str:
        
        split_list=s.split(" ")
        
        ans=[]
        for word in split_list:
            ans.append(word[::-1])
        
        return " ".join(ans)
        
        