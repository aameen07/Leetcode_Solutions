class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

# initially take maximum as -1
# reverse iteration
# new Max = max(oldMax, arr[i])
        
        rightMax=-1
        
        for i in range(len(arr)-1,-1,-1):
            newMax=max(rightMax,arr[i])
            arr[i]=rightMax
            rightMax=newMax
            
        return arr        

# hum arr ke end se iterate krte hue aenge and max pta lagate jaenge wahan se and jo unka max hai hr ek point pr usko us index ke element se compare krenge for getting max value