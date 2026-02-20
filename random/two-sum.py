class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # track numbers we've seen
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # found it if complement exists
            if complement in seen:
                return [seen[complement], i]
            
            # store current number and index
            seen[num] = i