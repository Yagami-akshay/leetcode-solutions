"""
04-best-time-to-buy-and-sell-stock.py
LeetCode Problem #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Arrays & Strings
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit from buying on one day and selling in the future.
        Uses a one-pass greedy approach tracking the minimum price seen so far.
        """
        if not prices:
            return 0

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# ==============================================================================
# Local Test Cases
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Typical case (fluctuating prices with profitable peak)
    prices1 = [7, 1, 5, 3, 6, 4]
    expected1 = 5  # Buy at 1, sell at 6 -> 6 - 1 = 5
    result1 = sol.maxProfit(prices1)
    print(f"Test 1 (Typical): prices={prices1}")
    print(f"  Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test 1 Failed: {result1} != {expected1}"
    print("  Status: PASSED\n")

    # Test Case 2: Edge case (strictly decreasing prices - no profit possible)
    prices2 = [7, 6, 4, 3, 1]
    expected2 = 0
    result2 = sol.maxProfit(prices2)
    print(f"Test 2 (Edge - Strictly Decreasing): prices={prices2}")
    print(f"  Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 Failed: {result2} != {expected2}"
    print("  Status: PASSED\n")

    # Test Case 3: Edge case (single price day - cannot buy and sell on different days)
    prices3 = [5]
    expected3 = 0
    result3 = sol.maxProfit(prices3)
    print(f"Test 3 (Edge - Single Element): prices={prices3}")
    print(f"  Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test 3 Failed: {result3} != {expected3}"
    print("  Status: PASSED\n")

    # Test Case 4: Edge case (identical prices throughout)
    prices4 = [3, 3, 3, 3]
    expected4 = 0
    result4 = sol.maxProfit(prices4)
    print(f"Test 4 (Edge - Flat Prices): prices={prices4}")
    print(f"  Expected: {expected4}, Got: {result4}")
    assert result4 == expected4, f"Test 4 Failed: {result4} != {expected4}"
    print("  Status: PASSED\n")

    print("All Best Time to Buy and Sell Stock tests passed successfully!")
