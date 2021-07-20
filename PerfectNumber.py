'''
507. Perfect Number
A Perfect Number s a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 6
Output: true
Example 3:

Input: num = 496
Output: true
Example 4:

Input: num = 8128
Output: true
Example 5:

Input: num = 2
Output: false
 

Constraints:

1 <= num <= 108
'''
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
        	return False
        result_sum = 0
        for val in range(1, int(math.sqrt(num)) + 1):
        	if num % val == 0:
        		if val == 1:        			
        			result_sum = result_sum + val
        			#print "1", result_sum
        		elif (val * val) != num:
        			result_sum = result_sum + val + (num // val)
        			#print "2", result_sum
        		else:
        			result_sum = result_sum + val
        			#print "3", result_sum

        if result_sum == num:
        	return True
        else:
        	return False

obj = Solution()
print(obj.checkPerfectNumber(16))
print(obj.checkPerfectNumber(2))
print(obj.checkPerfectNumber(496))
print(obj.checkPerfectNumber(8128))
