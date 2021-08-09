'''
Add Strings
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        len1 = len(num1)
        len2 = len(num2)

        if len1 < len2:
        	num1 = "0" * (len2 - len1) + num1
        if len1 > len2:
        	num2 = "0" * (len1 - len2) + num2
        len1 = len(num1)
        len2 = len(num2)
        result = ""
        for index in range(len1 - 1, -1, -1):
        	temp = ord(num1[index]) % 48 + ord(num2[index]) % 48 + carry
        	if temp > 9:
        		carry = 1
        	else:
        		carry = 0
        	result = str(temp % 10) + result

        if carry == 1:
        	return str(carry) + result
        else:
        	return result

obj = Solution()
print(obj.addStrings("11","123"))
print(obj.addStrings("456","77"))
print(obj.addStrings("0","0"))       