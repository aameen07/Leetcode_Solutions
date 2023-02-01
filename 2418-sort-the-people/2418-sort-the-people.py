class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d={}
        for i in range(len(names)):
            if heights[i] not in d:
                d[heights[i]] = names[i]
        
        # {180:Mary, 165 J, 170 E} 
        
        a = sorted(heights, key = lambda x: -x) #[180, 170, 165]
        
        for i,j in enumerate(a):    #enumerate gives i,j values where i would be index and j would                                        be the value at that index
            a[i] = d[j]             
            
            #we used enumerate here to save space so we dont have to create another list
        
        return a
        
        #cheers