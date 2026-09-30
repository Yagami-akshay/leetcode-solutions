"""
09-reverse-linked-list.py
LeetCode Problem #206: Reverse Linked List
Difficulty: Easy
Topic: Linked Lists (Bonus Problem)
"""

from typing import Optional, List


# Definition for singly-linked list node (standard LeetCode definition).
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly-linked list in-place iteratively.
        Uses 3 pointers (prev, curr, next_node) in O(n) time and O(1) space.
        """
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next  # Preserve remaining list
            curr.next = prev       # Reverse pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward

        return prev


# ==============================================================================
# Helper functions for local test execution
# ==============================================================================
def to_linked_list(elements: List[int]) -> Optional[ListNode]:
    """Builds a singly linked list from a Python list."""
    if not elements:
        return None
    head = ListNode(elements[0])
    curr = head
    for val in elements[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def to_python_list(head: Optional[ListNode]) -> List[int]:
    """Converts a singly linked list into a Python list for easy comparison."""
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case (multi-element list)
    input1 = [1, 2, 3, 4, 5]
    expected1 = [5, 4, 3, 2, 1]
    head1 = to_linked_list(input1)
    rev_head1 = sol.reverseList(head1)
    result1 = to_python_list(rev_head1)
    print(f"Test 1 (Typical - Multi-element): input={input1}")
    print(f"  Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (empty list)
    input2 = []
    expected2 = []
    head2 = to_linked_list(input2)
    rev_head2 = sol.reverseList(head2)
    result2 = to_python_list(rev_head2)
    print(f"Test 2 (Edge - Empty List): input={input2}")
    print(f"  Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (single-node list)
    input3 = [42]
    expected3 = [42]
    head3 = to_linked_list(input3)
    rev_head3 = sol.reverseList(head3)
    result3 = to_python_list(rev_head3)
    print(f"Test 3 (Edge - Single Element): input={input3}")
    print(f"  Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Two-element list
    input4 = [1, 2]
    expected4 = [2, 1]
    head4 = to_linked_list(input4)
    rev_head4 = sol.reverseList(head4)
    result4 = to_python_list(rev_head4)
    print(f"Test 4 (Edge - Two Elements): input={input4}")
    print(f"  Expected: {expected4}, Got: {result4}")
    assert result4 == expected4, f"Test 4 Failed: {result4} != {expected4}"
    print("  Status: PASSED\n")

    print("All Reverse Linked List tests passed successfully!")
