## Problem: Move Zeroes (Easy)
**Link:** [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)

### Approach
We use a two-pointer partitioning approach analogous to the partition step in Quicksort. A pointer `insert_pos` tracks where the next non-zero element should reside. As the loop pointer `i` scans through the array, whenever `nums[i] != 0`, we swap `nums[insert_pos]` with `nums[i]` and advance `insert_pos`. This automatically bubbles zeros toward the right while preserving the relative ordering of non-zero numbers.

### Complexity
- Time: O(n) — We make a single linear pass through the array of length $n$.
- Space: O(1) in-place — No auxiliary array or extra buffer is allocated; modifications occur directly in `nums`.

### Notes
A naive two-pass approach copies non-zeros first and then fills remaining cells with zeros. The swap technique achieves the exact same result in a single pass while minimizing the total number of write operations, especially when many non-zero elements are already at their correct positions.
