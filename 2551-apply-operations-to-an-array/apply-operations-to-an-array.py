class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0
        r = 1
        
        while r < len(nums):
            if nums[l] != nums[r]:
                l = r
                r += 1
            else: 
                nums[l] *= 2
                nums[r] = 0
                l = r
                r += 1

        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i]
                if l != i:
                    nums[i] = 0
                l += 1
        return nums

