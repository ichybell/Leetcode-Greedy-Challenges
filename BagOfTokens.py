"""
Bag of Tokens

You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

- If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
- If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible total score you can achieve after playing any number of tokens.

Example 1:

Input: tokens = [100], P = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up.

Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], P <= 10000
"""

# Solution:
# We use a greedy approach to solve this problem.
# Sort the tokens array in increasing order.
# We keep track of the current power and score.
# We also keep track of the start and end indices of the tokens array.
# While the start index is less than or equal to the end index, we do the following:
# - If the current power is greater than or equal to the value of the current start index,
# we play that token face up and update the power and score accordingly.
# We also increment the start index.
# - If the current score is greater than or equal to 1 and the current power is less than the value of the current start index,
# we play the token at the current end index face down and update the power and score accordingly.
# We also decrement the end index.
# -
# If we cannot play any token face up or face down, we break out of the loop.
# Return the final score.

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        power = P
        score = 0
        start = 0
        end = len(tokens) - 1
        while start <= end:
            if power >= tokens[start]:
                power -= tokens[start]
                score += 1
                start += 1
            elif score >= 1 and power < tokens[start]:
                power += tokens[end]
                score -= 1
                end -= 1
            else:
                break
        return score
