class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1



        while l <= r:
            mid = (r+l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                if target == nums[mid]:
                    return mid

        return -1
        # if l > 0 and nums[l - 1] == target:
        #     return left - 1
        # else:
        #     return -1