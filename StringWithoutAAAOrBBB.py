"""
String Without AAA or BBB

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:

Input: A = 4, B = 1
Output: "aabb"

Example 3:

Input: A = 2, B = 0
Output: "a"

Constraints:

0 <= A <= 100
0 <= B <= 100
"""

# Solution:
# We use a greedy approach to solve this problem.
# We start by adding the maximum number of 'a's and 'b's alternatingly until either A or B becomes 0.
# Then we add the remaining 'a's or 'b's.
# Return the string.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = []
        while A or B:
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = res[-1] == 'b'
            else:
                write_a = A >= B
            if write_a:
                A -= 1
                res.append('a')
            else:
                B -= 1
                res.append('b')
        return "".join(res)
