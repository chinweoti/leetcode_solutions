class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        nums.sort()

        for i, n in enumerate(nums):
            if nums[i]% 2 == 0:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l += 1
        return nums