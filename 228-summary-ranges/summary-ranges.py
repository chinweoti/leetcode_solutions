class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]  
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ranges.append(str(start) + "->" + str(nums[i]))
            else: 
                ranges.append(str(nums[i]))
            
            i += 1

        return ranges
        
        
        
        # res = []

        # l = 0
        # m = 0
        # r = 1

        # while r <= len(nums) and r+1 < len(nums):
        #     if nums[r] - nums[r-1] == 1:
        #         r += 1
        #     if  nums[r+1] - nums[r] != 1:
        #         res.append(str(nums[r]))
        #         l = r
        #         r += 1
        #     else:    
        #         res.append(str(nums[l]) + '->' + str(nums[r-1]))
        #         l = r
        #         r +=1
        #         print(l, r)
        # return res
