class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        counter = 1
        max_c = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                # print(nums[i], nums[i+1])
                counter +=  1
            else:
                counter = 1
            max_c = max(counter, max_c)
        return max_c