class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        # print(freq)
        res = []

        for e in range(1, len(nums)+1):
            # print(e)
            if e not in freq:
                res.append(e)
        return res
