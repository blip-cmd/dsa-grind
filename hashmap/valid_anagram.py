class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # return Counter(s) == Counter(t)

        # without the counter
        # we can create a map of s and for every letter found in t, we deduct in the map of s. we'd then sum up the dict.values. if it's > 0, we know one letter wasn't used in t

        if len(s) != len(t):
            return False
        
        hashmap ={}
        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1
        
        for x in t:
            if x not in hashmap or hashmap[x] == 0:
                return False
            hashmap[x] += -1
        
        return True
