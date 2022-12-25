"""
Task Scheduler

You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

"""

# Solution:
# We use a greedy approach to solve this problem.
# We create a heap and add all the characters to the heap.
# We pop the most frequent character from the heap and append it to the result string.
# We decrement the count of the character in the heap and push it back to the heap.
# If the heap is empty and there are still characters left in the result string, we return the length of the result string.
# If the heap is not empty, we append idle characters to the result string based on the value of n.

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        for c, count in Counter(tasks).items():
            heap.append((-count, c))
        heapq.heapify(heap)
        result = []
        while heap:
            count, c = heapq.heappop(heap)
            result.append(c)
            if heap and n > 0:
                result.extend(["idle"] * n)
            if -count > 1:
                heapq.heappush(heap, (count+1, c))
        return len(result)
