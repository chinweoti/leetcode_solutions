class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        result = defaultdict(int)
        # print(result)

        for i, n in enumerate(nums):
            result[n]= i

        for id, val in operations:
            nums[result[id]] = val
            result[val] = result[id]
        return nums