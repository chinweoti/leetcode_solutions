class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = (l + r)//2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else: 
                return mid

        return r

# if the sqrt of x is not in the range of x, at the end of the while loop, after the last number has been multiplied by itself and found to be greater than x, right pointer (r) will be updated to r= mid - 1, hence, the left pointer (l) would be greater than the right and the right would be the number closest to the sqrt rounded down
        