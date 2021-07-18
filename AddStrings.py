'''
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
        result = ""
        carry = "0"
        if len(num1) < len(num2):
        	num1 = ("0" * (len(num2) - len(num1))) + num1
        elif len(num1) > len(num2):
        	num2 = ("0" * (len(num1) - len(num2))) + num2
        for index in range(len(num1) - 1, -1, -1):
        	temp = (ord(carry) % 48) + (ord(num1[index]) % 48) + (ord(num2[index]) % 48)
        	if temp < 10:
        		result = chr(temp + 48) + result
        		carry = "0"
        	else:
        		carry = "1"
        		result = chr((temp % 10) + 48) + result
        if carry == "1":
        	result = carry + result
        return result

obj = Solution()
print(obj.addStrings("11", "12909"))
print(obj.addStrings("1", "999"))
print(obj.addStrings("456", "77"))
print(obj.addStrings("0", "0"))