class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        l=0
        r=len(s)
        
        longest_sub = ""
        
        for i in range(len(s)):
            for j in range(len(s),0,-1):
                
                sub = s[i:j]
                
                # print(sub)
                
                smallones = set(sub.lower())
                largesmallones = set(sub)
                
                # print(smallones,largesmallones)
                
                if len(largesmallones) == 2 * len(smallones):
                    
                    if len(sub) > len(longest_sub):
                        longest_sub = sub
        
        return longest_sub
        
        
        