class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # left pass
        n = len(nums)
        result = [1] * n
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        #right pass
        right_product= 1
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result


        # #my thoughts
        # without using the division operator defn includes  multiplying by a fraction.
        # my next thought is to find the product of nums.delete(item) each time and insert it after to maintain the index
        # # how about multiplying left side and right side 
            
        