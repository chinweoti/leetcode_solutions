class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        # print(freq)

        for k, v in freq.items():
            if v > 1:
                return k