class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
         #
        # #required:
        #     - take each positive integer in the list
        #     - reverse its digits and append to list.back
        #     - return n_distinct ints in the final array.

        # #1st approach
        # result = nums.copy() #O(n)
        # for x in nums: #O(n)
        #     new_x = int(str(x)[::-1]) #O(logx)
        #     result.append(new_x) #O(1) amortized
        # return(len(set(result)))  #O(n)
        # #time: O(n) + O(n.logx) +O(n) = O(n.logx)
        # #space: O(2n) + O(2n) + O(logx) = O(n)

        #2nd Approach
        # Using arithmetic conversion and 1 set from start
        seen = set(nums)  # O(n) to insert all original numbers

        for x in nums:    # O(n) iterations
            rev = 0
            temp = x
            while temp > 0:              # O(log x) - runs once per digit
                digit = temp % 10        # O(1) - modulo gives last digit
                rev = rev * 10 + digit   # O(1) - build reversed number
                temp //= 10              # O(1) - integer division removes last digit
            seen.add(rev)                # O(1) average - insert into set

        return len(seen)  # O(1) - length retrieval

        # time: O(n) + O(n.logx) + O(n) = O(n.logx)
        # space: O(n) + O(n) + O(logx) = O(n)

