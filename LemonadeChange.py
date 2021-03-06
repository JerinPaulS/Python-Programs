'''
860. Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with correct change, or false otherwise.

 

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.
Example 3:

Input: bills = [5,5,10]
Output: true
Example 4:

Input: bills = [10,10]
Output: false
 

Constraints:

1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.
'''
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_count = 0
        ten_count = 0
        twenty_count = 0
        for note in bills:
        	if note == 5:
        		five_count = five_count + 1
        	elif note == 10:
        		ten_count = ten_count + 1
        		if five_count <= 0:
        			return False
        		else:
        			five_count = five_count - 1
        	else:
        		twenty_count = twenty_count + 1
        		if ten_count <= 0:
        			if five_count < 3:
        				return False
        			else:
        				five_count = five_count - 3
        		elif five_count <= 0:
        			return False
        		else:
        			ten_count = ten_count - 1
        			five_count = five_count - 1
        return True

obj = Solution()
print(obj.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))        