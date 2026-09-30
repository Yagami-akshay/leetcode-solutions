## Problem: Binary Search (Easy)
**Link:** [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)

### Approach
We implement the classic divide-and-conquer binary search algorithm over a sorted array. Maintaining two pointers `left = 0` and `right = len(nums) - 1`, we repeatedly compute the midpoint `mid = left + (right - left) // 2`. We compare `nums[mid]` with `target`: if equal, we return `mid`; if smaller, the target must lie in the right half (`left = mid + 1`); otherwise, it lies in the left half (`right = mid - 1`).

### Complexity
- Time: O(log n) — The search space is halved in each step until either the target is located or the boundaries cross.
- Space: O(1) — The iterative approach executes in-place without recursion stack overhead.

### Notes
Using `left + (right - left) // 2` rather than `(left + right) // 2` is a standard best practice to prevent arithmetic overflow in fixed-width integer languages (like C/C++ or Java). Even in Python's arbitrary-precision integers, adhering to this pattern reinforces robust systems-level habits.
