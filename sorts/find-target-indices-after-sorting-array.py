class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # results = []
        # for i,x in enumerate(nums):
        #     if x == target:
        #         results.append(i)
        # return(results)

        less = 0 
        equal = 0
        for i,x in enumerate(nums):
            if x < target:
                less += 1
            elif x == target:
                equal += 1

        return (list(range(less, less+equal)))
        
        