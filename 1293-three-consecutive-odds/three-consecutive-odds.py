class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0

        for e in arr:
            if e % 2 != 0:
                counter += 1
                print(e, counter)
            elif e % 2 == 0 and counter < 3: 
                counter = 0
                print(counter)
            
        return counter >= 3