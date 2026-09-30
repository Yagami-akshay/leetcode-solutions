## Problem: Valid Parentheses (Easy)
**Link:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

### Approach
We use a stack data structure following the Last-In-First-Out (LIFO) principle alongside a hash table mapping closing brackets to their expected opening counterparts (`{')': '(', '}': '{', ']': '['}`). Opening brackets are pushed onto the stack. When encountering a closing bracket, we pop the top element from the stack (or use a dummy sentinel if empty) and verify it matches the corresponding opening symbol; if mismatched or if unclosed brackets remain on the stack at the end, the string is invalid.

### Complexity
- Time: O(n) — We traverse the input string of length $n$ once, performing $O(1)$ push and pop operations on the stack.
- Space: O(n) — In the worst-case scenario (e.g. `((((((`), the stack accommodates up to $n$ characters.

### Notes
Handling boundary edge cases like empty stacks when encountering closing brackets (`]`) and remaining unclosed brackets (`(`) requires both checking emptiness during popping and asserting that `len(stack) == 0` upon terminating the loop.
