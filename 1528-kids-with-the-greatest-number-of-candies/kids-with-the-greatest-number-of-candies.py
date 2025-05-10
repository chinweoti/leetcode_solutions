class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for e in candies:
            res.append(e + extraCandies >= max_candies)
        return res
        
            