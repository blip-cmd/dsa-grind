class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # int arr is incrasing
        # left+right = target, l<r
        # res = [l+1,r+1]
        # O(1) extra space -> no new containers

        n = len(numbers)
        l,r =0,n-1

        while l < r:
            #cehck sum
            p1 = numbers[l]
            p2 = numbers[r]
            _sum = p1+p2
            if _sum  == target:
                return [l+1,r+1]

            #increment
            if _sum > target:
                r = r-1
            else:
                l = l+1
            
        # return res