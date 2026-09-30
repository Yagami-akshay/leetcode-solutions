"""
01-two-sum.py
LeetCode Problem #1: Two Sum
Difficulty: Easy
Topic: Arrays & Strings
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds indices of the two numbers such that they add up to target.
        Uses a one-pass hash map to achieve O(n) time complexity.
        """
        seen = {}  # maps value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case (distinct positive numbers)
    nums1, target1 = [2, 7, 11, 15], 9
    expected1 = [0, 1]
    result1 = sol.twoSum(nums1, target1)
    print(f"Test 1 (Typical): nums={nums1}, target={target1}")
    print(f"  Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (duplicate numbers forming the target sum)
    nums2, target2 = [3, 3], 6
    expected2 = [0, 1]
    result2 = sol.twoSum(nums2, target2)
    print(f"Test 2 (Edge - Duplicates): nums={nums2}, target={target2}")
    print(f"  Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (negative numbers)
    nums3, target3 = [-3, 4, 3, 90], 0
    expected3 = [0, 2]
    result3 = sol.twoSum(nums3, target3)
    print(f"Test 3 (Edge - Negative/Zero sum): nums={nums3}, target={target3}")
    print(f"  Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    print("All Two Sum tests passed successfully!")
