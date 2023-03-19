class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # i=0
        # while(i<len(arr)):
        #     if arr[i]==0:
        #         arr.pop()
        #         arr.insert(i,0)
        #         i+=1
        #     i+=1
        
        
        zeros=0
        for a in arr:
            if a==0:
                zeros+=1
        
        i=len(arr)-1
        j=len(arr)-1+zeros
        
        while(i!=j):
            self.insert(arr,i,j)
            if arr[i]==0:
                j-=1
                self.insert(arr,i,j)
            i-=1
            j-=1
        
        return arr
    

    def insert(self,arr,i,j):
        if j<len(arr):
            arr[j]=arr[i]
            
            
            
            
            