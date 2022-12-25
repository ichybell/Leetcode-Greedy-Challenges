"""
Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true

Example 4:

Input: nums = [1,2,1,2,1,2,1,2], k = 2
Output: true

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""

# Solution:
# We can use a greedy approach to solve this problem.
# We will sort the array first and then for each element we will check if the element and the next k-1 elements are consecutive or not.
# If they are not consecutive then we return false.
# If we reach the end of the array we return true.

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums) and nums[j] == nums[j-1]+1:
                j += 1
            if j-i < k:
                return False
            i = j
        return True
