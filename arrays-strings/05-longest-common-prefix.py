"""
05-longest-common-prefix.py
LeetCode Problem #14: Longest Common Prefix
Difficulty: Easy
Topic: Arrays & Strings
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string amongst an array of strings.
        Uses vertical scanning across characters at matching indices.
        """
        if not strs:
            return ""

        # Scan column by column using the first string as reference
        for col in range(len(strs[0])):
            char = strs[0][col]
            for row in range(1, len(strs)):
                # If current string is shorter than col, or character mismatches
                if col >= len(strs[row]) or strs[row][col] != char:
                    return strs[0][:col]

        return strs[0]


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case with common prefix
    strs1 = ["flower", "flow", "flight"]
    expected1 = "fl"
    result1 = sol.longestCommonPrefix(strs1)
    print(f"Test 1 (Typical): strs={strs1}")
    print(f"  Expected: '{expected1}', Got: '{result1}'")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (no common prefix)
    strs2 = ["dog", "racecar", "car"]
    expected2 = ""
    result2 = sol.longestCommonPrefix(strs2)
    print(f"Test 2 (Edge - No Common Prefix): strs={strs2}")
    print(f"  Expected: '{expected2}', Got: '{result2}'")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (single word in list)
    strs3 = ["alone"]
    expected3 = "alone"
    result3 = sol.longestCommonPrefix(strs3)
    print(f"Test 3 (Edge - Single Word): strs={strs3}")
    print(f"  Expected: '{expected3}', Got: '{result3}'")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Edge case (empty string in input list)
    strs4 = ["", "b", "c"]
    expected4 = ""
    result4 = sol.longestCommonPrefix(strs4)
    print(f"Test 4 (Edge - Contains Empty String): strs={strs4}")
    print(f"  Expected: '{expected4}', Got: '{result4}'")
    assert result4 == expected4, f"Test 4 Failed: {result4} != {expected4}"
    print("  Status: PASSED\n")

    print("All Longest Common Prefix tests passed successfully!")
