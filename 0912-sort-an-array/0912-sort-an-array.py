class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_values=self.merge_sort(nums)
        return sorted_values
    
    def merge_sort(self,arr):
        
        if len(arr)==1:
            return arr
        
        mid = len(arr)//2
        
        left=arr[:mid]
        right=arr[mid:]
        
        left_value = self.merge_sort(left)
        right_value = self.merge_sort(right)
        
        sortof=[]
        l=0
        r=0
        
        while l<len(left_value) and r<len(right_value):
            if left_value[l]<right_value[r]:
                sortof.append(left_value[l])
                l+=1
            else:
                sortof.append(right_value[r])
                r+=1
        while l<len(left_value):
            sortof.append(left_value[l])
            l+=1
        while r<len(right_value):
            sortof.append(right_value[r])
            r+=1
            
        return sortof
        
        