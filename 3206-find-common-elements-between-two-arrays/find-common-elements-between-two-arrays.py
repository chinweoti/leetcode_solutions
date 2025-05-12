class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = 0
        counter2 = 0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                counter1 += 1
        
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                counter2 += 1
        return [counter1, counter2]
