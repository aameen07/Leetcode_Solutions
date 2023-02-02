class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # for i in range(len(words)):
        #     if len(words[i])<len(words[0]):
        #         return False
            
        d= { x:y for y,x in enumerate(order)}
        
        for j in range(len(words)-1):
            a = words[j]
            b = words[j+1]
            flag = False
            
            for w1, w2 in zip(a,b):
                if d[w1]<d[w2]:
                    flag = True
                    break
                elif d[w1]>d[w2]:
                    return False
            
            if not flag and len(a)>len(b):
                return False
            
        return True
                    