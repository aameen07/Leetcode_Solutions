class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        a=""
        for r in range(len(word)):
            if word[r]==ch:
                a+=word[:r+1]
                a=a[::-1]
                a+=word[r+1:]        
                return a
        
        return word