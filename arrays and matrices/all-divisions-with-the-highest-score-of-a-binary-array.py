class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #vars
        n = len(nums)
        left_zeros = 0 
        right_ones = sum(nums) #binary array
        _max = - 1
        result = []

        #check each possible split
        for i in range(n+1):
            score = left_zeros + right_ones
            if score > _max:
                _max = score
                result = [i] #reset answer
            elif score == _max:
                result.append(i) #build answer
            
            if i < n:  #bound check
                #update counters
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1
        
        return result