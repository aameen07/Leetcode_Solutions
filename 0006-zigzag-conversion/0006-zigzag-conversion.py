class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if (numRows<2):
            return s
        
        arr=[""]*numRows
        direction=False         # False means When going DOWN , True means when going UP
        row = 0
        for i in s:
            arr[row]+=i
            if row == numRows-1:            # yahan se
                direction = True            #
            elif row == 0:            # 
                direction = False            # yahan tk direction change kr rhe hai sirf
            
            if (direction == False):
                row+=1
            else:
                row-=1
        
        return ("".join(arr))
    