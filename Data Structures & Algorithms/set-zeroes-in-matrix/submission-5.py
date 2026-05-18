class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        row_zero = False
        col_zero = False

        for col in range(cols):
            if matrix[0][col] == 0:
                row_zero = True

        for row in range(rows):
            if matrix[row][0] ==0:
                col_zero = True     

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] ==0 or matrix[0][col]==0:
                    matrix[row][col] = 0

        
        if col_zero:
            for r in range(rows):
                matrix[r][0] = 0

            
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        