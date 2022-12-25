"""
Lemonade Change

At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: [5,5,10]
Output: true

Example 3:

Input: [10,10]
Output: false

Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.

"""

# Solution:
# We use a greedy approach to solve this problem.
# We start with 0 fives and 0 tens.
# For every customer, we check if the bill is a $5 bill.
# If it is, we increment the count of fives.
# If it is a $10 bill, we decrement the count of fives and increment the count of tens.
# If it is a $20 bill, we decrement the count of tens and decrement the count of fives by 2.
# If at any point, the count of fives or tens becomes negative, we return false.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -= 1
                tens += 1
            elif bill == 20:
                if tens:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0 or tens < 0:
                return False
        return True
