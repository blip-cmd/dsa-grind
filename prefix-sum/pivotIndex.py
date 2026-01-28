class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # sum all the numbers. start on left.
        # remove current item from sum
        # check if left_sum(starts at 0) =  main_sum.
        #     else next index:
        #         reduce main sum by index item
        #         add leaving index item to left sum
        #         check left_sum and right sum. repeat till end of array.

        # is this efficient enough?
        # or i should think of a better approach.

        