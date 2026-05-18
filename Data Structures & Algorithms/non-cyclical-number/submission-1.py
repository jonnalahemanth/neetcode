class Solution:
    def isHappy(self, n: int) -> bool:

        def square(k:int):
                res =0
                while k>0:
                        digit = k %10
                        res += digit*digit
                        k = k//10
                return res

        
        seen = set()

        while n != 1 and n not in seen:
                seen.add(n)
                n = square(n)
                

        
        return n == 1
        