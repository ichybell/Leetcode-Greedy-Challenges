"""
Wiggle Subsequence

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative.
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

"""

# Solution:
# We use a greedy approach to solve this problem.
# We start with a base case where the first element is the start of the wiggle subsequence.
# We then iterate through the rest of the array and check if the current element is greater than the previous element.
# If it is, we update the previous element to be the current element and increment the count.
# If it is not, we check if the current element is less than the previous element.
# If it is, we update the previous element to be the current element and increment the count.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        prev, count = nums[0], 1
        for i in range(1, n):
            if nums[i] > prev:
                prev = nums[i]
                count += 1
            elif nums[i] < prev:
                prev = nums[i]
                count += 1
        return count