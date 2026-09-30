## Problem: Two Sum (Easy)
**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

### Approach
A brute-force comparison of all pairs requires $O(n^2)$ time. Instead, we use a one-pass hash map (`seen`) to store each number and its index as we traverse the array. For each element `num`, we check if its complement (`target - num`) already exists in the dictionary, allowing instantaneous $O(1)$ lookups and finding the pair in a single pass.

### Complexity
- Time: O(n) — Each lookup and insertion in the hash table takes $O(1)$ average time, and we iterate through the list of length $n$ at most once.
- Space: O(n) — In the worst case, we store up to $n$ elements in the dictionary.

### Notes
Handling duplicate elements was a key edge case: if `nums = [3, 3]` and `target = 6`, looking up the complement *before* adding the current element into the dictionary prevents overwriting the previous index and cleanly captures both distinct indices without additional logic.
