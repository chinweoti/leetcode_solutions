class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0

        for e in nums:
            if e < 0:
                neg += 1
            elif e > 0:
                pos += 1
            elif e == 0:
                continue
            # res = max(pos, neg)
        return max(pos, neg)
