'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
        	flag = 1
        	x = x * (-1)
        n = x
        rev = 0
        while n > 0:
        	rem = n % 10
        	rev = (rev * 10) + rem
        	n = int(n/10)
        if flag == 1:
        	rev = rev * (-1)
        if rev < -(2**31) or rev > (2**31) - 1:
        	rev = 0
        print(rev)

    reverse(object, 1534236469)
    reverse(object, -123)