"""
02-reverse-string.py
LeetCode Problem #344: Reverse String
Difficulty: Easy
Topic: Arrays & Strings
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses an array of characters in-place using two pointers.
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case (odd length string)
    s1 = ["h", "e", "l", "l", "o"]
    expected1 = ["o", "l", "l", "e", "h"]
    print(f"Test 1 (Typical): Input = {s1}")
    sol.reverseString(s1)
    print(f"  Expected: {expected1}, Got: {s1}")
    assert s1 == expected1, f"Test 1 Failed: {s1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (single element list)
    s2 = ["a"]
    expected2 = ["a"]
    print(f"Test 2 (Edge - Single Element): Input = {s2}")
    sol.reverseString(s2)
    print(f"  Expected: {expected2}, Got: {s2}")
    assert s2 == expected2, f"Test 2 Failed: {s2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (even length palindrome)
    s3 = ["H", "a", "n", "n", "a", "h"]
    expected3 = ["h", "a", "n", "n", "a", "H"]
    print(f"Test 3 (Edge - Even Length): Input = {s3}")
    sol.reverseString(s3)
    print(f"  Expected: {expected3}, Got: {s3}")
    assert s3 == expected3, f"Test 3 Failed: {s3} != {expected3}"
    print("  Status: PASSED\n")

    print("All Reverse String tests passed successfully!")
