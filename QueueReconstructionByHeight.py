"""
Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""

# Solution:
# We use a greedy approach to solve this problem.
# We first sort the array in non-increasing order of the height.
# For those with the same height, we sort in non-decreasing order of the number of people in front.
# We then iterate through the sorted array and insert each element at the kth position in the result array.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result