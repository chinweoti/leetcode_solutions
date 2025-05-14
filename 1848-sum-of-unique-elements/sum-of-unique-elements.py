class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        sums = 0

        for e in nums:
            dict[e] += 1
        
        for key, value in dict.items():
            if value == 1:
                sums += key

        return sums
