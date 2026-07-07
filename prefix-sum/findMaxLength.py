class Solution(object):
    def findMaxLength(self, nums):
        lookup = {0: -1}
        cur_sum = max_len = 0
        for i, n in enumerate(nums):
            cur_sum += 1 if n == 1 else -1
            if cur_sum in lookup:
                max_len = max(max_len, i - lookup[cur_sum])
            else:
                lookup[cur_sum] = i
        return max_len