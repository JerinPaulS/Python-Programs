'''
264. Ugly Number II
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]

        ptr1 = 0
        ptr2 = 0
        ptr3 = 0
        num1 = 2
        num2 = 3
        num3 = 5

        for num in range(n):
        	val = min(num1, num2, num3)
        	dp.append(val)
        	if val == num1:
        		ptr1 = ptr1 + 1
        	if val == num2:
        		ptr2 = ptr2 + 1
        	if val == num3:
        		ptr3 = ptr3 + 1
        	num1, num2, num3 = dp[ptr1] * 2, dp[ptr2] * 3, dp[ptr3] * 5
        return dp[n - 1]