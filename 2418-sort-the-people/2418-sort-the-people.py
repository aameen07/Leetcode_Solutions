class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d={}
        for i in range(len(names)):
            if heights[i] not in d:
                d[heights[i]] = names[i]
        
        # {180:Mary, 165 J, 170 E} 
        
        heights = sorted(heights, key = lambda x: -x) #[180, 170, 165]
        
        for i,j in enumerate(heights):
            heights[i] = d[j]
        
        return heights
        