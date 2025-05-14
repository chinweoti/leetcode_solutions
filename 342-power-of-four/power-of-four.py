class Solution:
    import math
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            if n <= 0:
                return False

        x = 4**round(math.log(n, 4))
        return x == n