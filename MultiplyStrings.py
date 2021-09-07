'''
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''
class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if num1 == "0" or num2 == "0":
			return "0"
		result = ""
		count = -1
		for a in num1[::-1]:
			carry = 0
			temp = ""
			count = count + 1
			for b in num2[::-1]:
				res = carry + ((ord(a) - ord("0")) * (ord(b) - ord("0")))
				if res > 9:
					carry = res // 10
				else:
					carry = 0
				temp = str(res % 10) + temp

			if carry != 0:
				temp = str(carry) + temp
			if result == "":
				result = temp
			else:
				result = self.string_add(result, temp + ("0" * count))
		index = 0
		while index < len(result):
			if result[index] == "0":
				index = index + 1
			else:
				break
		return result[index:]

	def string_add(self, a, b):
		a_len = len(a)
		b_len = len(b)
		max_len = 0
		if a_len < b_len:
			a = "0" * (b_len - a_len) + a
			max_len = b_len
		else:
			b = "0" * (a_len - b_len) + b
			max_len = a_len
		result = ""
		carry = 0
		for index in range(max_len - 1, -1, -1):
			res = carry + ((ord(a[index]) - ord("0")) + (ord(b[index]) - ord("0")))
			if res > 9:
				carry = 1
			else:
				carry = 0
			result = str(res % 10) + result
		if carry == 1:
			result = "1" + result
		return result

obj = Solution()
print(obj.multiply("99", "91"))