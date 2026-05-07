class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(text):
            left, right= 0, len(text)-1

            while left<=right:
                if text[left]!=text[right]:
                    return False
                left += 1
                right -= 1

            return True

        
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])

            for end in range(start, len(s)):
                string = s[start:end+1]
                if is_palindrome(string):
                    path.append(string)
                    backtrack(end+1, path)
                    path.pop()
            
        backtrack(0, [])
        return res

        