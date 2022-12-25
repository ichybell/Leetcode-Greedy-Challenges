"""
Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        visited = set()
        for c in s:
            count[c] -= 1
            if c in visited:
                continue
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return "".join(stack)
