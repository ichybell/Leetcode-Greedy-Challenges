"""
Jump Game

Problem Description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

## Example

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index."""


# Solution

# To solve this problem, we can use a greedy approach.

# We start by keeping track of the maximum index that we can reach at each step. 
# If the maximum index is greater than or equal to the last index, we return True.
# If the maximum index is less than the last index, we return False.

# To update the maximum index, we can simply take the maximum of the current maximum index and the current index plus the maximum jump length at the current index.

# This solution has a time complexity of O(n) and a space complexity of O(1).


# Code
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, jump in enumerate(nums):
            if max_index >= len(nums) - 1:
                return True
            if i > max_index:
                return False
            max_index = max(max_index, i + jump)
        return True
