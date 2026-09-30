## Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Approach
We iterate through the price history once while dynamically maintaining the lowest purchase price observed so far (`min_price`). At each day $i$, we evaluate the profit yielded if we sold on that day (`prices[i] - min_price`) and update `max_profit` if this value exceeds previous records. This greedy single-pass strategy eliminates nested loop comparisons.

### Complexity
- Time: O(n) — We traverse the price list of length $n$ exactly once.
- Space: O(1) — We maintain only two scalar variables (`min_price` and `max_profit`).

### Notes
A key edge case is a monotonic downward trend (e.g. `[7, 6, 4, 3, 1]`) where every transaction yields a loss; initializing `max_profit` to `0` naturally handles this requirement without requiring conditional branching at the end.
