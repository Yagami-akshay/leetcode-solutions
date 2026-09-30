## Problem: Longest Common Prefix (Easy)
**Link:** [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)

### Approach
We use a vertical scanning approach, comparing characters at the same index across all strings column by column. Taking the first string `strs[0]` as our benchmark, we check each character position: if any subsequent string is shorter than the current index or contains a mismatch, we immediately truncate and return the prefix matched up to that column.

### Complexity
- Time: O(S) — In the worst case where all strings are identical, we compare all characters ($S$ being the total character count across all strings). In typical cases with early mismatches, runtime is bounded by $O(n \cdot m)$ where $m$ is the length of the shortest string.
- Space: O(1) auxiliary — Only index pointers are maintained during scanning; the returned prefix substring uses negligible slice memory.

### Notes
Handling lists with an empty string `""` or words of differing lengths required index boundary guards (`col >= len(strs[row])`) prior to character comparison to prevent `IndexError` exceptions.
