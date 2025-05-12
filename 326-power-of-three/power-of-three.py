class Solution:
    import math
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1





        # if n <= 0:
        #     return False
        # log_val = math.log(n, 3)
        # return abs(round(log_val) - log_val) < 1e-10