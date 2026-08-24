class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # vars
        left_index, right_index = 0, len(nums) - 1
        mid_index = 0

        # loop
        while left_index <= right_index:
            mid_index = left_index + (right_index - left_index) // 2

            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        # not found
        return -1


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Target exists in the middle/right
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    res1 = solution.search(nums1, target1)
    print(f"Test 1 - nums: {nums1}, target: {target1} -> index: {res1}")
    assert res1 == 4

    # Test Case 2: Target does not exist
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    res2 = solution.search(nums2, target2)
    print(f"Test 2 - nums: {nums2}, target: {target2} -> index: {res2}")
    assert res2 == -1

    # Test Case 3: Single-element array where element is target (tests <= boundary)
    nums3 = [5]
    target3 = 5
    res3 = solution.search(nums3, target3)
    print(f"Test 3 - nums: {nums3}, target: {target3} -> index: {res3}")
    assert res3 == 0

    # Test Case 4: Single-element array where element is not target
    nums4 = [5]
    target4 = 1
    res4 = solution.search(nums4, target4)
    print(f"Test 4 - nums: {nums4}, target: {target4} -> index: {res4}")
    assert res4 == -1


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/binary-search/
# key: binary search, two pointers, divide and conquer
# notes: Maintain closed interval [left, right]. Mid calculation avoids integer overflow. Halve the search space each step.
# space: O(1). Uses constant extra space for index pointers.
# time: O(log n). Divides the search range by half on each iteration.
