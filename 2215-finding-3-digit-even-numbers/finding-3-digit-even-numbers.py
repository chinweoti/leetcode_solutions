class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        res = []
        for num in range(100, 1000, 2):
            ab, c = divmod(num, 10)
            a, b = divmod(ab, 10)
            freq[a] -= 1
            freq[b] -= 1
            freq[c] -= 1
            if freq[a] >= 0 and freq[b] >= 0 and freq[c] >= 0:
                res.append(num)
            freq[a] += 1
            freq[b] += 1
            freq[c] += 1
        return res