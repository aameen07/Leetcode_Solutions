class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        
        if len(sentence)<26:
            return False
        
        d=collections.Counter(sentence)
        # print(d)
        
        if len(d) == 26:
            return True
        