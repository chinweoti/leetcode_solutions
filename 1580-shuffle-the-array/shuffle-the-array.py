class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = len(nums)//2
        res= []

        while i <= j and j < len(nums):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1

        return res