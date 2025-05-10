class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        l = 0 
        r = 0
        n = len(nums)

        while r < n:
            if abs(l - r) >= indexDifference and abs(nums[l] - nums[r]) >= valueDifference:
                return[l, r]
            r += 1
            if r == n and l < n - 1:
                l += 1
                r = l    
        return [-1, -1]




        # for i, vi in enumerate(nums):
        #     for j, vj in enumerate(nums):
        #         if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
        #             return [i,j]
        # return [-1,-1]