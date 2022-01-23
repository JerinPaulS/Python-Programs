'''
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
'''
class Solution:
	def sequentialDigits(self, low, high):
		digits = "123456789"

		def find(num):
			count = 0
			while num > 0:
				count += 1
				num = num // 10
			return count

		min_len = find(low)
		max_len = find(high)
		res = []
		result = []


		for leng in range(min_len, max_len + 1):
			for index in range(leng, len(digits) + 1):
				temp = digits[index - leng:index]
				res.append(int(digits[index - leng:index]))

		for num in res:
			if low <= num <= high:
				result.append(num)

		return result

obj = Solution()
print(obj.sequentialDigits(1000, 13000))        