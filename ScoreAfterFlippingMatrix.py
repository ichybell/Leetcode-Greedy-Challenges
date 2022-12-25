"""
Score After Flipping Matrix

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

"""

# Solution:
# We use a greedy approach to solve this problem.
# For each row, if the number of 1s is greater than the number of 0s, we flip the row.
# For each column, if the number of 1s is greater than the number of 0s, we flip the column.
# We return the sum of all rows.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] = 1 - A[i][j]
        for j in range(m):
            count = 0
            for i in range(n):
                count += A[i][j]
            if count <= n//2:
                for i in range(n):
                    A[i][j] = 1 - A[i][j]
        result = 0
        for i in range(n):
            result += int("".join(str(x) for x in A[i]), 2)
        return result
