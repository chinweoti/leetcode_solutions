class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        x_counter = 1
        y_counter = 1
        max_counter = 1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                x_counter += 1
                y_counter = 1
            elif nums[i] > nums[i+1]:
                y_counter += 1
                x_counter = 1
            else: 
                x_counter = 1
                y_counter = 1
            max_counter = max(max_counter, x_counter, y_counter)
        return max_counter
            