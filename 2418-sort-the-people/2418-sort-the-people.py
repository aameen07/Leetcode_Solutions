class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d={}
        for i in range(len(names)):
            if heights[i] not in d:
                d[heights[i]] = names[i]
        
        # {180:Mary, 165 J, 170 E} 
        
        a = sorted(heights, key = lambda x: -x)
        
        for i,j in enumerate(a):
            a[i] = d[j]
        
        return a
        