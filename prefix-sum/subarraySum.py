class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # brute force 
        # check each possible subarray and sum. and count sums matching given k

        # result = 0
        
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i,len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             result += 1

        # return result
        
        #optimized using hashmap to store cumulative sum frequencies
        result = 0
        prefix_dict = {0:1}
        running_sum = 0 
        for i in range(len(nums)):
            running_sum += nums[i]
            dif = running_sum - k
            result += prefix_dict.get(dif,0)
            prefix_dict[running_sum] = 1 + prefix_dict.get(running_sum, 0) 
        
        return result