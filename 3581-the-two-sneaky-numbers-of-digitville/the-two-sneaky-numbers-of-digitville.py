class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for e in nums:
            freq[e] = freq.get(e, 0)+1
        
        for k, v in freq.items():
            if v == 2:
                res.append(k)
        return res
