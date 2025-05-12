class Solution:
    import math
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        # return n.is_integer()


        l = 1
        r = num

        while l <= r:
            mid = (l+r)//2
            if mid > n:
                r = mid - 1
            elif mid < n:
                l = mid + 1
            else:
                return True
        return False

