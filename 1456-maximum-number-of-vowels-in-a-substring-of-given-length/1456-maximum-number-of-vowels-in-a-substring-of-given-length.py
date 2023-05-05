class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel="aeiou"
        count=0
        maxcount=0
        
        for i in range(len(s)):
            if s[i] in vowel:
                count+=1
                
                
            if i>=k and s[i-k] in vowel:
                count-=1
                
            maxcount = max(maxcount,count)
        
        return maxcount
                
                
                