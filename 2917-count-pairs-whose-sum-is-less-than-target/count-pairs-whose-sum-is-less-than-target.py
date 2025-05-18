class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        l = 0
        r =  n-1
        while l < r:
            if nums[l] + nums[r] < target:
                ans += (r - l)
                # use ans += (r-l) since the array is sorted anything in between will match the condition less than target
                # as l closes to r in the array (l-r) produces all combinations of l and r less than the target
                l +=1
            else:
                r -=1
        return ans
