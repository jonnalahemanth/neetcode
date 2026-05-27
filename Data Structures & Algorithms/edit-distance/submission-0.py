class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                ans = dfs(i+1, j+1)
            
            else:
                insert = 1+dfs(i, j+1)
                delete = 1+dfs(i+1, j)
                replace = 1+dfs(i+1, j+1)

                ans = min(insert, delete, replace)

            dp[(i, j)] = ans
            return ans
        
        return dfs(0, 0)
