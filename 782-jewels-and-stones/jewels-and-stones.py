class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dicts = Counter(stones)
        count = 0
        for k, v in dicts.items():
            if k in jewels:
                count += v
        return count