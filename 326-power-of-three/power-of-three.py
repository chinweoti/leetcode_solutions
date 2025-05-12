class Solution:
    import math
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3**round(math.log(n, 3)) == n 



        # while n>=1:
        #     if n == 1:    
        #         return True
        #     n = n/3
        # return False



        # if n <= 0:
        #     return False
        # while n % 3 == 0:
        #     n = n // 3
        # return n == 1



        # if n <= 0:
        #     return false
        # if 3**19 % n == 0:
        #     return True
        # return False



        # if n <= 0:
        #     return False
        # log_val = math.log(n, 3)
        # return abs(round(log_val) - log_val) < 1e-10