"""
Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

"""

# Solution:
# We use a greedy approach to solve this problem.
# We create a dictionary to store the last index of each character.
# We iterate through the string and keep track of the maximum index we have seen so far.
# Whenever we see a character whose last index is equal to the maximum index seen so far, we add the length of the partition to the result list and reset the start of the next partition to be the index after the current one.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(S):
            last_index[c] = i
        result = []
        start = 0
        max_index = 0
        for i, c in enumerate(S):
            max_index = max(max_index, last_index[c])
            if i == max_index:
                result.append(i - start + 1)
                start = i + 1
        return result
