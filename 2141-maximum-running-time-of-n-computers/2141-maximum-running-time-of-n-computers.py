class Solution:
    def maxRunTime(self, n: int, bat: List[int]) -> int:
        
        bat.sort()
        s=sum(bat)
        while bat[-1] > s//n:
            n-=1
            s-=bat.pop()
        
        return s//n
        