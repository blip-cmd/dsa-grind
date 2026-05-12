class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # no duplicates

        n = len(s)
        l= 0
        #use a set to track
        seen = set()
        _max = 1 #least possible

        for r in range(n):
            while s[r] in seen:
                #keep right still, shrink left
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            _max =max(_max, r-l+1)

        return _max

