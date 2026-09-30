"""
08-valid-parentheses.py
LeetCode Problem #20: Valid Parentheses
Difficulty: Easy
Topic: Stacks
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string containing brackets '()[]{}' is valid.
        Uses a Last-In-First-Out (LIFO) stack to match closing brackets with their openings.
        """
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_map:
                # Closing bracket encountered
                top_element = stack.pop() if stack else "#"
                if bracket_map[char] != top_element:
                    return False
            else:
                # Opening bracket encountered
                stack.append(char)

        # Valid only if all opened brackets were successfully matched and closed
        return not stack


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case (simple valid pair sequence)
    s1 = "()[]{}"
    expected1 = True
    result1 = sol.isValid(s1)
    print(f"Test 1 (Typical - Simple Sequence): s='{s1}'")
    print(f"  Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Typical case (nested valid brackets)
    s2 = "{[()]}"
    expected2 = True
    result2 = sol.isValid(s2)
    print(f"Test 2 (Typical - Nested): s='{s2}'")
    print(f"  Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (single opening bracket - stack remains non-empty)
    s3 = "("
    expected3 = False
    result3 = sol.isValid(s3)
    print(f"Test 3 (Edge - Single Opening): s='{s3}'")
    print(f"  Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Edge case (interleaved invalid bracket order)
    s4 = "([)]"
    expected4 = False
    result4 = sol.isValid(s4)
    print(f"Test 4 (Edge - Interleaved/Mismatched): s='{s4}'")
    print(f"  Expected: {expected4}, Got: {result4}")
    assert result4 == expected4, f"Test 4 Failed: {result4} != {expected4}"
    print("  Status: PASSED\n")

    # Test Case 5: Edge case (starts with closing bracket - pop on empty stack)
    s5 = "]"
    expected5 = False
    result5 = sol.isValid(s5)
    print(f"Test 5 (Edge - Leading Closing Bracket): s='{s5}'")
    print(f"  Expected: {expected5}, Got: {result5}")
    assert result5 == expected5, f"Test 5 Failed: {result5} != {expected5}"
    print("  Status: PASSED\n")

    print("All Valid Parentheses tests passed successfully!")
