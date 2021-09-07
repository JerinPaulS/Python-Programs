'''
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            b = 0
            while dividend >= divisor << b:
                b = b + 1
            dividend = dividend - (divisor << b - 1)
            result = result + (1 << b - 1)
        if sign:
            result = 0 - result
        return min(max(result, -2 ** 31), (2 ** 31) - 1)


obj = Solution()
print(obj.divide(10, -3))
		'''
		if dividend == -2147483648 and divisor == -1:
            return 2147483647
        result, sign = 0, 1
        if dividend < 0:
            dividend, sign = -dividend, -sign
        if divisor < 0:
            divisor, sign = -divisor, -sign
        if dividend == divisor:
            return sign
        while dividend >= divisor:
            b = 0
            while dividend >= divisor << b:
                b = b + 1
            dividend = dividend - (divisor << b - 1)
            result = result + (1 << b - 1)
        if sign < 0:
            return -result
        else:
            return result
        '''  