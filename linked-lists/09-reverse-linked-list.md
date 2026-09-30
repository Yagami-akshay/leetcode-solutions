## Problem: Reverse Linked List (Easy)
**Link:** [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)

### Approach
We reverse the singly linked list using an in-place iterative 3-pointer pattern (`prev`, `curr`, `next_node`). We initialize `prev = None` and `curr = head`. At each step, we temporarily preserve the reference to `curr.next`, redirect `curr.next` to point back to `prev`, advance `prev` to `curr`, and advance `curr` to the preserved next node. Once `curr` becomes `None`, `prev` points to the new head of the reversed list.

### Complexity
- Time: O(n) — Each node in the list of length $n$ is visited exactly once.
- Space: O(1) in-place — Reversal is performed purely by modifying existing node pointers, requiring zero extra dynamic memory.

### Notes
Remembering to store `curr.next` before overwriting it is critical to avoid disconnecting and losing access to the tail of the list. Boundary cases including empty lists (`head = None`) and single-node lists (`head.next = None`) execute seamlessly without requiring special-case branches.
