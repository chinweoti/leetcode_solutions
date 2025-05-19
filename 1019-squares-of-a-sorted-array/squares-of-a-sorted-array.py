class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] **= 2
        return sorted(nums)























        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2
        # nums.sort()
        # return nums
             