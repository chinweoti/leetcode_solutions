class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sums = 0

        for e in nums:
            if nums.count(e) == 1:
                sums += e

        return sums
