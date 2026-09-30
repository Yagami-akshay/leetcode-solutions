"""
06-binary-search.py
LeetCode Problem #704: Binary Search
Difficulty: Easy
Topic: Basic Algorithms
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in a sorted ascending array of integers in O(log n) time.
        Returns the index of target if found, otherwise returns -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Prevents integer overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case (element exists in middle of array)
    nums1, target1 = [-1, 0, 3, 5, 9, 12], 9
    expected1 = 4
    result1 = sol.search(nums1, target1)
    print(f"Test 1 (Typical - Found): nums={nums1}, target={target1}")
    print(f"  Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Element does not exist in array
    nums2, target2 = [-1, 0, 3, 5, 9, 12], 2
    expected2 = -1
    result2 = sol.search(nums2, target2)
    print(f"Test 2 (Typical - Not Found): nums={nums2}, target={target2}")
    print(f"  Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (single element array - target matches)
    nums3, target3 = [5], 5
    expected3 = 0
    result3 = sol.search(nums3, target3)
    print(f"Test 3 (Edge - Single Element Match): nums={nums3}, target={target3}")
    print(f"  Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Edge case (single element array - target does not match)
    nums4, target4 = [5], -5
    expected4 = -1
    result4 = sol.search(nums4, target4)
    print(f"Test 4 (Edge - Single Element Mismatch): nums={nums4}, target={target4}")
    print(f"  Expected: {expected4}, Got: {result4}")
    assert result4 == expected4, f"Test 4 Failed: {result4} != {expected4}"
    print("  Status: PASSED\n")

    print("All Binary Search tests passed successfully!")
