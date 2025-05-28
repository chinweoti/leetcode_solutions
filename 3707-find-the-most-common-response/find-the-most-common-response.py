class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = defaultdict(int)

        for response in responses:
            for each in set(response):
                freq[each] += 1
                # print(freq)
        
        for k, v in freq.items():
            max_freq = max(freq.values())
            # print(max_freq)
            final = [k for k, v in freq.items() if v == max_freq]
            # print(final)
            return min(final)
