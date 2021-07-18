'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        mid = int((start + end) / 2)
        while(start <= end):
        	mid = int((start + end) / 2)
        	if mid * mid < x:
        		start = mid + 1
        	elif mid * mid == x:
        		return(mid)
        	else:
        		end = mid - 1
        if mid * mid == x:
        	return(mid)
        else:
        	return(start - 1)

obj = Solution()
print(obj.mySqrt(4))
print(obj.mySqrt(8))
print(obj.mySqrt(5))
print(obj.mySqrt(12))
print(obj.mySqrt(26))
print(obj.mySqrt(35))