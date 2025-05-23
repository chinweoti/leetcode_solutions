class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        

        for i, n in enumerate(nums):
            if nums[i]% 2 == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return nums
        # if you dont want a temp holder, exchange both in one line ie nums[l], nums[i] = nums[i], nums[l]
        # time complexity = O(n)
        # space complexity = O(1)
        # sort operation is logarithmic


        # l, r = 0, len(nums) - 1
        # while l < r:
        #     if nums[l] % 2 == 0:
        #         l += 1
        #     elif nums[r] % 2 != 0:
        #         r -= 1
        #     else:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         left += 1
        #         right -= 1
        # return nums