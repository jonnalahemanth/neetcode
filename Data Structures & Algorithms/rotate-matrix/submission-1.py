class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def transpose(mat):
            n = len(mat)

            for i in range(n):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j] 
        

        def reverse(mat):
            n = len(mat)

            for row in range(n):
                for i in range(n//2):
                    mat[row][i], mat[row][n-i-1] = mat[row][n-i-1], mat[row][i]



        transpose(matrix)
        reverse(matrix)