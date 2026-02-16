class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

    # THE IDEA
    #Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    # Output: [[1,2],[3,10],[12,16]]

    #step1. add pairs that have an end lesser than the newIntervals start.
    # res = [1,2]

    #step2. check and merge all overlaps into one pair
    #new_pair = [4,8] overlaps with [3,5] so becomes [3,8]
    # [3,8] overlaps with 6,7 -> 3,8
    # 3,8 overlaps with [8,10] -> 3,10
    # so new_pair becomes [3,10] and is added to the res : res = [1,2],[3,10]

    # no overlaps left, append the remaining pairs.
    # res = [1,2],[3,10],[12,16]

        #python

        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1] :
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            
            i += 1
            
        result.append(newInterval)

        while i<n:
            result.append(intervals[i])
            i += 1

        return result
       