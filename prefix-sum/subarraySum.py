class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #brute force 
        # check each possible subarray and sum. and count sums matching given k

        result = 0
        
        for i in range(len(nums)):
            total = 0
            for j in range(i,len(nums)):
                total += nums[j]
                if total == k:
                    result += 1
                    
        return result
        