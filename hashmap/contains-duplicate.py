class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #one liner
        return len(nums) != len(set(nums))

        # seen = set()
        
        # for x in nums:
        #     if x in seen:
        #         return True
        #     seen.add(x)
            
        # return False