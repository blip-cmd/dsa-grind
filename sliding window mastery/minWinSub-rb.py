from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #HARD
        
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
        
        res,res_len = [-1,-1], float('inf')
        
        