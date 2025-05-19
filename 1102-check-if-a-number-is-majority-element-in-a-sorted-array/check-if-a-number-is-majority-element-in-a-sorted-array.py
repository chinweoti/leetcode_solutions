class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        maj_e = Counter(nums)
        n = len(nums)/2


        if maj_e[target] > n: 
            return True
        return False