class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        for ind, n in enumerate(nums):
            if n == key:
                res.append(ind)
        result = []
        for i in range(len(nums)):
            for j in res:
                if abs(i - j) <= k:
                    result.append(i)
                    break
        return sorted(result)
        

