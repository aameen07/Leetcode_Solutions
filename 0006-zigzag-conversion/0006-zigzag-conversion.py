class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if (numRows<2):
            return s
        
        arr=[""]*numRows
        direction=False
        row = 0
        for i in s:
            arr[row]+=i
            if row == numRows-1:
                direction = True
            elif row == 0:
                direction = False
            
            if (direction == False):
                row+=1
            else:
                row-=1
        
        return ("".join(arr))
    