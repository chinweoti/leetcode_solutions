class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0

        for e in nums:
            if e == 1:
                counter += 1
            else:
                counter = 0
            max_counter = max(max_counter, counter)
        return max_counter
