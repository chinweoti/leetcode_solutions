class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for e in range(0, n+1):
            if e not in nums:
                return e
        # return 0