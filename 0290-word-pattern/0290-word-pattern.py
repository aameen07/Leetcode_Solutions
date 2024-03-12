class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        p=list(pattern)
        s=s.split()
        d={}
        
        if len(s)!=len(p): return False
        if len(set(s))!=len(set(p)): return False
        
        for i , val in enumerate(p):
            if val in d and d[val]!=s[i]:
                return False
            else:
                d[val]=s[i]
                
        return True

# or

#         words = s.split(" ")
#         if len(pattern) != len(words):
#             return False
#         charToWord = {}
#         wordToChar = {}
        
#         for c, w in zip(pattern, words):
#             if c in charToWord and charToWord[c] != w:
#                 return False
#             if w in wordToChar and wordToChar[w] != c:
#                 return False
#             charToWord[c] = w
#             wordToChar[w] = c
#         return True

        