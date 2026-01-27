class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
       #net gain at i -> cumulative sum to the point 
        #we are to calculate all altitudes but return the highest.
       #start at 0 and expand r right. adjust local sum based on value entering and update global highest altitude

       #code

        max_height_point = 0
        max_height = 0
        height = 0
        for r in range(len(gain)):
            height = height + gain[r]
            if height > max_height:
                max_height_point = r
                max_height = max(height, max_height)

        return gain[max_height_point]