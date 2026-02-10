class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Found out this would only work on sorted arrays not this unsorted version of the problem
        # n = len(nums)
        # l,r = 0, n-1
        # while l < r:
        #     total  = nums[l] + nums[r]

        #     if total == target:
        #         return [l,r]
        #     elif total > target:
        #         r -=1
        #     else:
        #         l +=1

        #using a dictionary to store a difference and location
        hashmap ={}
        for i, x in enumerate(nums):
            difference = target - x
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[x] = i