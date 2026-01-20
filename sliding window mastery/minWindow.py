class Solution:
    def characterReplacement(self, s, k):
        count = {}
        max_len = 0
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # 1. Update the frequency of the current character
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # 2. Update max_freq (highest frequency seen so far)
            max_freq = max(max_freq, count[s[right]])
            
            # 3. Check if the current window is invalid
            if (right - left + 1) - max_freq > k:
                # 4. If invalid, "slide" the window by moving the left pointer
                count[s[left]] -= 1
                left += 1
                
            # 5. Capture the maximum length
            max_len = max(max_len, right - left + 1)
            
        return max_len

# # realizations
# identifying the invalid state first
# Comparing an if and while per the problem when contracting
# best way to update your trackers. eg. finding this maximum, u don't always have to update it, u need the overall maximum not that of every window
# checking and avoiding O(n) method calls like dict.values() in a loop.
# use python's dict.get() to avoid null errors
# converting the challenge to a program_pattern is like 60% of the effort.