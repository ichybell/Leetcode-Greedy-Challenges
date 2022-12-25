"""
Minimum Add to Make Parentheses Valid

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1

Example 2:

Input: "((("
Output: 3

Example 3:

Input: "()"
Output: 0

Example 4:

Input: "()))(("
Output: 4

Note:

S.length <= 1000
S only consists of '(' and ')' characters.

"""

# Solution:
# We use a greedy approach to solve this problem.
# We keep a count of the number of open parentheses.
# If we see an open parentheses, we increment the count.
# If we see a close parentheses, we decrement the count.
# If the count becomes negative, we add an open parentheses and increment the count.
# We return the absolute value of the count at the end.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        result = 0
        for c in S:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    result += 1
                    count = 0
        return result + abs(count)
