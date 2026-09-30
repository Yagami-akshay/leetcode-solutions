"""
07-move-zeroes.py
LeetCode Problem #283: Move Zeroes
Difficulty: Easy
Topic: Basic Algorithms
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0's to the end of nums while maintaining relative order of non-zero elements.
        Modifies nums in-place in O(n) time and O(1) space.
        """
        insert_pos = 0

        # Swap non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case with mixed zeros and non-zeros
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    print(f"Test 1 (Typical): Input = {nums1}")
    sol.moveZeroes(nums1)
    print(f"  Expected: {expected1}, Got: {nums1}")
    assert nums1 == expected1, f"Test 1 Failed: {nums1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (single zero)
    nums2 = [0]
    expected2 = [0]
    print(f"Test 2 (Edge - Single Zero): Input = {nums2}")
    sol.moveZeroes(nums2)
    print(f"  Expected: {expected2}, Got: {nums2}")
    assert nums2 == expected2, f"Test 2 Failed: {nums2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (no zeros in array)
    nums3 = [1, 2, 3, 4]
    expected3 = [1, 2, 3, 4]
    print(f"Test 3 (Edge - No Zeros): Input = {nums3}")
    sol.moveZeroes(nums3)
    print(f"  Expected: {expected3}, Got: {nums3}")
    assert nums3 == expected3, f"Test 3 Failed: {nums3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Edge case (all zeros)
    nums4 = [0, 0, 0]
    expected4 = [0, 0, 0]
    print(f"Test 4 (Edge - All Zeros): Input = {nums4}")
    sol.moveZeroes(nums4)
    print(f"  Expected: {expected4}, Got: {nums4}")
    assert nums4 == expected4, f"Test 4 Failed: {nums4} != {expected4}"
    print("  Status: PASSED\n")

    print("All Move Zeroes tests passed successfully!")
