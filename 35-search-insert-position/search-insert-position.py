class Solution:
    from bisect import bisect_left
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums, target)
        return index
        # time complexity is O(log n)

        # l = 0 
        # r = len(nums) -1

        # while l <= r:
        #     mid = (l + r)//2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else: 
        #         return mid
        # return l
        # time complexity is O(log n)