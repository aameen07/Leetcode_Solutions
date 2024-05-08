class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or 
                   board[r][c] in squares[(r//3,c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
        return True
    
    
# We make Dictionary of row number as keys and the value as the set of the values which are there in that row now after that we do the same for columns and then we do the same for squares. We check if the element has already been in that row or column or in that square(for square we use r//3,c//3 to get which sqaure it is) and then if its not there we add it and the end since there are no mistakes we give True that its a vald Sudoku.