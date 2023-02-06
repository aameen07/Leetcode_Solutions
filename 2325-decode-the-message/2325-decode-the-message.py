class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        l= string.ascii_lowercase
        i=0
        for j in (key):
            if j not in d and j !=" ":
                d[j]=l[i]
                i+=1
        
        a = ""
        for i in message:
            if i == " ":
                a+=" "
            else:
                a+=d[i]
            
        return a  
                