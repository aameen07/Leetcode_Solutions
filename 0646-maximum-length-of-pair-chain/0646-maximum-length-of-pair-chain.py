class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pairs = sorted(pairs, key=lambda x: x[1])
        pairs.sort(key=lambda x:x[1])
        res=0
        cur=-math.inf
        for head, tail in pairs:
            if head>cur:
                cur=tail
                res+=1
        
        return res
        
        
        