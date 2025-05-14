class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # follow up
        # this approach is better if nums1 is small compared to nums2
        # this approach is also better for limited memory and if nums2 is stored on a disk
        h_map = defaultdict(int)
        result = []

        for e in nums1:
            h_map[e] += 1
            print(h_map)

        for e in nums2:
            if h_map[e] > 0:
                print(e)
                result.append(e)
                h_map[e] -= 1
        return result




        # # follow up
        # # if array is sorted 
        # # use two-pointer approach:
        # i = 0
        # j = 0
        # res =[]
        # nums1 = sorted(nums1)
        # nums2 = sorted(nums2)

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         res.append(nums1[i])
        #         i += 1
        #         j += 1
        # return res
