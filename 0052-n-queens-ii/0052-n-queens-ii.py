class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        pos=set() #r+c
        neg=set() #r-c
        
        res=[]
        board=[["."]*n for i in range(n)]
        
        self.dfs(0,col,pos,neg,board,n,res)
        return len(res)
    
    def dfs(self,r,col,pos,neg,board,n,res):
        if r==n:
            copy=["".join(i) for i in board]
            res.append(copy)
            return 
        
        for c in range(n):
            if c in col or r+c in pos or r-c in neg:
                continue
            
            col.add(c)
            pos.add(r+c)
            neg.add(r-c)
            board[r][c]="Q"
            
            self.dfs(r+1,col,pos,neg,board,n,res)
            
            col.remove(c)
            pos.remove(r+c)
            neg.remove(r-c)
            board[r][c]="."
            
            
            