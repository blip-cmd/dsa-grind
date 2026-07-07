from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        # 1. Setup requirements
        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0
        
        # Tracking the best window: (length, left, right)
        res = float("inf"), 0, 0
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            have[char] = 1 + have.get(char, 0)
            
            # If this char completes the requirement for a specific letter in T
            if char in need and have[char] == need[char]:
                formed += 1
            
            # 2. Try to shrink the window from the left while it's valid
            while formed == required:
                # Update result if this window is smaller than previous best
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)
                
                # Remove left char to try and find a smaller window
                left_char = s[l]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                
                l += 1
        
        # 3. Return the substring if we found one
        length, l, r = res
        return s[l : r + 1] if length != float("inf") else ""