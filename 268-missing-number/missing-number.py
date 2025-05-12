class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # for e in range(0, n+1):
        #     if e not in nums:
        #         return e




        n = len(nums)
        sorted_nums = sorted(nums)
        if(sorted_nums[0]!= 0):
            return 0
        elif(sorted_nums[-1] != n):
            return n
        for i in range(0, n+1):
            if(sorted_nums[i]!=i):
                return i