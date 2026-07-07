from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #tier1
        
        #vars
        #target_counts: dictionary to store t letters and counts
        #window_counts: dictionary to store what we have
        #array to hold indices, and pointers of current result 
        #have: an integer of how many found unique t characters are in the substring
        #need: an integer of how many unique t characters are needed
        
        #process
        #expand right till window is valid
            # it's valid when have == need
        #shrink left as much as possible
        
        #We don't increment have just because a character exists; we increment it only when a specific requirement is met
        
        #setup
        if not t or not s: return ""
        
        target_counts = Counter(t)
        window_counts = {}
        have = 0
        need = len(target_counts)
        
        res,res_len = [0,-1], float('inf')
        l = res[0]
        
        #iterate
        for r in range(len(s)):
            char = s[r]
            #update dict
            window_counts[char] = 1 + window_counts.get(char, 0)
            
            #check if valid
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1
            
            #minimize when valid
            while have == need:
                #update result only if smaller window is found
                if (r-l+1) < res_len:
                    res_len = min((r-l+1), res_len)
                    res = [l,r]
            
                char_l = s[l]
                window_counts[char_l] -=  1
                
                if char_l in  target_counts and window_counts[char_l] < target_counts[char_l]:
                    have -= 1
                
                
                l += 1
        
        return s[res[0]:res[1]+1] if res_len != float('inf') else ""