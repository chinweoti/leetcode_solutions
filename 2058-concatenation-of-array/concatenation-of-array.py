class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # res = []

        # for e in nums:
        #     res.append(e)
        # for i in nums:
        #     res.append(i)
        # return res



        nums.extend(nums)

        return nums
