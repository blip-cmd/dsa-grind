class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #starting at ends.
        #setup
        l = 0
        n = len(numbers)
        r = n - 1
        # r = min(bisect.bisect_right(numbers, target-numbers[l]) , len(numbers)-1) #bisect_right good for very large data where target is not near the right end. 


        while l < r:
        #iterate
            left = numbers[l]
            right = numbers[r]
            total = left+right

            if total == target:
                return [l+1,r+1]
            elif total > target:
                r = r-1
            elif total < target:
                l = l+1