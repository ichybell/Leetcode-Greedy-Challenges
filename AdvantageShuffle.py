"""
Advantage Shuffle

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9

"""

# Solution:
# We use a greedy approach to solve this problem.
# We sort the A array in decreasing order.
# We iterate through the B array and for each element we find the smallest element in A that is greater than the current element in B.
# We remove this element from A and append it to the result array.
# If we reach the end of A and there are still elements in B, we append the remaining elements of A to the result array.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort(reverse=True)
        result = []
        for b in B:
            i = bisect_left(A, b)
            if i == len(A):
                result.append(A.pop())
            else:
                result.append(A.pop(i))
        return result + A
