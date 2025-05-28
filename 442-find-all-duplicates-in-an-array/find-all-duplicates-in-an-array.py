class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []

        for k, v in freq.items():
            if v == 2:
                res.append(k)
        return res