class Solution:
    import math
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        return n.is_integer()
