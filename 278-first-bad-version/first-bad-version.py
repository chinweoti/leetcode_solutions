# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= n:
            mid = (l+r)//2
            if not isBadVersion(mid):
                l = mid + 1
            elif isBadVersion(mid -1):
                 r = mid - 1
            else:
                return mid
