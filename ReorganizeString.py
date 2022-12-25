"""
Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

S will consist of lowercase letters and have length in range [1, 500].

"""

# Solution:
# We use a greedy approach to solve this problem.
# We create a heap and add all the characters to the heap.
# We pop the two most frequent characters from the heap and append them to the result string.
# If the heap is empty and there are still characters left in the result string, we return an empty string.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        for c, count in Counter(S).items():
            heap.append((-count, c))
        heapq.heapify(heap)
        result = []
        while heap:
            count1, c1 = heapq.heappop(heap)
            if not heap:
                if -count1 > 1:
                    return ""
                result.append(c1)
                break
            count2, c2 = heapq.heappop(heap)
            result.extend([c1, c2])
            if -count1 > 1:
                heapq.heappush(heap, (count1+1, c1))
            if -count2 > 1:
                heapq.heappush(heap, (count2+1, c2))
        return "".join(result)
