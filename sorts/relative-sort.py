class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Step 1: Count everything in arr1
        counts = collections.Counter(arr1)
        res = []
        
        # Step 2: Add elements in the order they appear in arr2
        for x in arr2:
            if x in counts:
                res.extend([x] * counts.pop(x))
        
        # Step 3: Sort the remaining elements (leftovers)
        # sorted(counts.keys()) gives us the remaining numbers in ascending order
        leftovers = sorted(counts.elements())
        res.extend(leftovers)
        
        return res