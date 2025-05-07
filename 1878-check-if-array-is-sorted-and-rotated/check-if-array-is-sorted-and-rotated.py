class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 1

        for i in range(1, 2* N):
            if nums[(i-1) % N] <= nums[i % N]:
                count += 1
            else:
                count = 1
            if count == N:
                return True
        return N == 1


        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] > nums[(i + 1) % len(nums)]:
        #         count += 1
        #     if count > 1:
        #         return False
        # return True