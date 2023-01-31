class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        a=""
        string2=[]
        string1= s.split(" ")
        for i in range(k):
            string2.append(string1[i])
        string1=" ".join(string2)
        return (string1)