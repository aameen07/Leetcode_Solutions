class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        a=""
        for r in range(len(word)):
            if word[r]==ch:
                a+=word[:r+1]
                # a=a[::-1]
                # a+=word[r+1:] 
                a=self.reverse(a)+word[r+1:]
                return a
        
        return word
        
    
    def reverse(self,a):
        b=[]
        for i in a:
            b.append(i)
    
        l=0
        r=len(b)-1
        while(l<r):
            c=b[l]
            b[l]=b[r]
            b[r]=c

            l+=1
            r-=1
        c=""
        for i in range(len(b)):
            c+=b[i]    
               
        return c