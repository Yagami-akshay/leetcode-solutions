# LeetCode Solutions & Practice Log

**Student Name:** Akshay N  
**SRN:** R25EF021  
**Course:** Portfolio Building for Engineering Students — GitHub-Integrated Edition (B25GE0101)  
**Semester:** 3rd Semester, CSE

---

> **Personal LeetCode practice log — part of B25GE0101 portfolio**

---

## 📌 Table of Contents

- [Overview & Methodology](#-overview--methodology)
- [Topic Directories](#-topic-directories)
  - [1. Arrays & Strings](arrays-strings/)
  - [2. Basic Algorithms](basic-algorithms/)
  - [3. Stacks](stacks/)
  - [4. Linked Lists](linked-lists/)
- [Curated Problem Set](#-curated-problem-set)
- [Local Testing & Verification](#-local-testing--verification)
- [Progress Log](#-progress-log)
- [How to Run Tests](#-how-to-run-tests)

---

## 📖 Overview & Methodology

This repository serves as a version-controlled portfolio artifact demonstrating disciplined algorithm practice, problem-solving methodologies, and clean code principles.

Rather than submitting unverified code directly to an online judge, every problem in this repository adheres to a strict engineering workflow:
1. **Understand & Analyze:** Read the problem statement, identify edge cases, and define input constraints.
2. **Develop Solution Locally:** Write the complete solution in VS Code using Python 3 with clean separation of logic and typing.
3. **Local Test Suites:** Implement at least 2 distinct test cases per problem (`main()` execution block) covering both typical happy-path inputs and boundary edge cases (e.g., duplicates, single-element collections, empty/null values, negative numbers).
4. **Local Verification:** Run and pass all assertions locally prior to LeetCode submission.
5. **Documentation & Analysis:** Document each solution with concise approach notes, time and space complexity derivations, and insights learned.
6. **Submission Verification:** Verify against LeetCode's online judge and archive the submission verification badge.

---

## 📂 Topic Directories

| Directory | Topic Area | Focus Concepts |
| :--- | :--- | :--- |
| [📁 `arrays-strings/`](arrays-strings/) | Arrays & Strings | Hash map lookups, two pointers, in-place manipulation, prefix scanning, greedy scanning |
| [📁 `basic-algorithms/`](basic-algorithms/) | Basic Algorithms | Binary search ($O(\log n)$ bounds), two-pointer partitioning |
| [📁 `stacks/`](stacks/) | Stacks | LIFO data structures, delimiter matching, bracket balancing |
| [📁 `linked-lists/`](linked-lists/) | Linked Lists | Pointer manipulation, iterative list reversal |

---

## 🧩 Curated Problem Set

| # | Problem | Topic | Difficulty | Solution | Documentation | Verification |
| :-: | :--- | :--- | :-: | :---: | :---: | :---: |
| 01 | [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays & Strings | Easy | [`01-two-sum.py`](arrays-strings/01-two-sum.py) | [`01-two-sum.md`](arrays-strings/01-two-sum.md) | [Accepted](arrays-strings/01-result.png) |
| 02 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Arrays & Strings | Easy | [`02-reverse-string.py`](arrays-strings/02-reverse-string.py) | [`02-reverse-string.md`](arrays-strings/02-reverse-string.md) | [Accepted](arrays-strings/02-result.png) |
| 03 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Arrays & Strings | Easy | [`03-valid-anagram.py`](arrays-strings/03-valid-anagram.py) | [`03-valid-anagram.md`](arrays-strings/03-valid-anagram.md) | [Accepted](arrays-strings/03-result.png) |
| 04 | [Best Time to Buy & Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Arrays & Strings | Easy | [`04-best-time-to-buy-and-sell-stock.py`](arrays-strings/04-best-time-to-buy-and-sell-stock.py) | [`04-best-time-to-buy-and-sell-stock.md`](arrays-strings/04-best-time-to-buy-and-sell-stock.md) | [Accepted](arrays-strings/04-result.png) |
| 05 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Arrays & Strings | Easy | [`05-longest-common-prefix.py`](arrays-strings/05-longest-common-prefix.py) | [`05-longest-common-prefix.md`](arrays-strings/05-longest-common-prefix.md) | [Accepted](arrays-strings/05-result.png) |
| 06 | [Binary Search](https://leetcode.com/problems/binary-search/) | Basic Algorithms | Easy | [`06-binary-search.py`](basic-algorithms/06-binary-search.py) | [`06-binary-search.md`](basic-algorithms/06-binary-search.md) | [Accepted](basic-algorithms/06-result.png) |
| 07 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Basic Algorithms | Easy | [`07-move-zeroes.py`](basic-algorithms/07-move-zeroes.py) | [`07-move-zeroes.md`](basic-algorithms/07-move-zeroes.md) | [Accepted](basic-algorithms/07-result.png) |
| 08 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stacks | Easy | [`08-valid-parentheses.py`](stacks/08-valid-parentheses.py) | [`08-valid-parentheses.md`](stacks/08-valid-parentheses.md) | [Accepted](stacks/08-result.png) |
| 09 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) *(Bonus)* | Linked Lists | Easy | [`09-reverse-linked-list.py`](linked-lists/09-reverse-linked-list.py) | [`09-reverse-linked-list.md`](linked-lists/09-reverse-linked-list.md) | [Accepted](linked-lists/09-result.png) |

---

## 🧪 Local Testing & Verification

Each solution file contains standalone, executable test cases with zero external dependencies. To run all test cases for any solution:

```bash
# Example: Running Two Sum test suite
python arrays-strings/01-two-sum.py

# Example: Running Valid Parentheses test suite
python stacks/08-valid-parentheses.py
```

---

## 📊 Progress Log

Detailed session timings and progress tracking are documented in [**`PROGRESS.md`**](PROGRESS.md).
