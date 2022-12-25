"""
Previous Permutation With One Swap

Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, return the same array.

Example 1:

Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.

Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.

Example 3:

Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.

Example 4:

Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.

Note:

1 <= A.length <= 10000
1 <= A[i] <= 10000
"""

# Solution:
# We use a greedy approach to solve this problem.
# Traverse the array from right to left.
# When we find a decreasing element, let it be A[i], we find the next maximum element in the subarray A[i+1:]
# and swap them.
# Return the modified array.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                for j in range(len(A) - 1, i, -1):
                    if A[j] < A[i]:
                        break
                    if A[j] == A[i]:
                        j -= 1
                        break
                A[i], A[j] = A[j], A[i]
                break
        return A
