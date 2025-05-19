class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(num for num in nums if num%2 == 0 )
        

        if not freq:
            return -1

        max_freq = max(freq.values())
    
        m_freq = [k for k, v in freq.items() if v == max_freq]
        # print(m_freq)
        return min(m_freq)
        