class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []

        for k, v in freq.items():
            if v == 2:
                res.append(k)

        for i in range(1, len(nums)+1):
            if i not in freq:
                res.append(i)
        return res
                