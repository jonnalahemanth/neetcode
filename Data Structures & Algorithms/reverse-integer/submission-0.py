class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**31 - 1
        check = limit // 10
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            # overflow check
            if res > check or (res == check and digit > 7):
                return 0

            res = res * 10 + digit

        return sign * res
        