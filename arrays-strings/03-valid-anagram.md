## Problem: Valid Anagram (Easy)
**Link:** [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

### Approach
Two strings are anagrams if and only if they possess identical character frequencies. We first perform an $O(1)$ fast check on string lengths; if `len(s) != len(t)`, they cannot be anagrams. Next, we tally character occurrences in `s` into a frequency hash map and decrement the counts while iterating through `t`, immediately returning `False` if any character count drops below zero or is missing.

### Complexity
- Time: O(n) — We traverse strings `s` and `t` of length $n$ once, performing $O(1)$ hash map operations.
- Space: O(1) auxiliary — Because the problem is constrained to lowercase English letters (26 characters), the hash table size is bounded by a constant $O(k)$ where $k \le 26$.

### Notes
Checking length equality upfront eliminates unnecessary hash table allocations for mismatched inputs. While `sorted(s) == sorted(t)` offers a one-liner solution, it runs in $O(n \log n)$ time, making the frequency-counting hash map approach superior in asymptotic time efficiency.
