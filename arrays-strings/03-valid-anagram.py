"""
03-valid-anagram.py
LeetCode Problem #242: Valid Anagram
Difficulty: Easy
Topic: Arrays & Strings
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if t is an anagram of s.
        Checks lengths first, then compares character frequency counts.
        """
        if len(s) != len(t):
            return False

        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        for char in t:
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1

        return True


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical positive case
    s1, t1 = "anagram", "nagaram"
    expected1 = True
    result1 = sol.isAnagram(s1, t1)
    print(f"Test 1 (Typical - Anagram): s='{s1}', t='{t1}'")
    print(f"  Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (different lengths)
    s2, t2 = "a", "ab"
    expected2 = False
    result2 = sol.isAnagram(s2, t2)
    print(f"Test 2 (Edge - Different Lengths): s='{s2}', t='{t2}'")
    print(f"  Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (same length, different characters)
    s3, t3 = "rat", "car"
    expected3 = False
    result3 = sol.isAnagram(s3, t3)
    print(f"Test 3 (Edge - Mismatched Characters): s='{s3}', t='{t3}'")
    print(f"  Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Edge case (single identical character)
    s4, t4 = "z", "z"
    expected4 = True
    result4 = sol.isAnagram(s4, t4)
    print(f"Test 4 (Edge - Single Character Match): s='{s4}', t='{t4}'")
    print(f"  Expected: {expected4}, Got: {result4}")
    assert result4 == expected4, f"Test 4 Failed: {result4} != {expected4}"
    print("  Status: PASSED\n")

    print("All Valid Anagram tests passed successfully!")
