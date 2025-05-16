class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)
        odd_count = 0
        for count in counts.values():
            if count % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True