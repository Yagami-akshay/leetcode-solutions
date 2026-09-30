## Problem: Reverse String (Easy)
**Link:** [https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/)

### Approach
We use the two-pointer technique to reverse the array in place without allocating auxiliary memory. One pointer begins at index `0` and another at `len(s) - 1`. In each iteration, we swap the characters at both pointers and step inward until the two pointers meet or cross.

### Complexity
- Time: O(n) — We perform $n / 2$ swaps, visiting each element once.
- Space: O(1) — Reversal is performed in-place with only two pointer variables.

### Notes
Remembering that Python strings are immutable was an important language distinction; here the input is passed as a mutable `List[str]`, which allows genuine $O(1)$ in-place swaps rather than creating a new string copy.
