class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else: 
                    a.append(board[i][j])
            if len(a) != len(set(a)):
                return False
            a = []
                
        b = []
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else: 
                    b.append(board[j][i])
                
            if len(b) != len(set(b)):
                return False
            b = []
    
        c = []
        for row in range(0,9,3):
            for col in range(0,9,3):

                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if board[j][i] == ".":
                            continue
                        else: 
                            c.append(board[j][i])
                
                if len(c) != len(set(c)):
                    return False
                c = []


        return True
