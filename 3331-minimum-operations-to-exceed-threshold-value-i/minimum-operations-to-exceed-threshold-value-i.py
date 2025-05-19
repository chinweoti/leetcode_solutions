class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0

        for e in nums:
            if e < k:
                counter += 1
        return counter