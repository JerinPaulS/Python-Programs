'''
Circular Prime Number 
A prime number is a Circular Prime Number if all of its possible rotations are itself prime numbers. Now given a number N check if it is Circular Prime or Not.
 

Example 1:

Input: N = 197
Output: 1
Explanation: 197 is a Circular Prime because
all rotations of 197 are 197, 719, 971 all of 
the 3 are prime number's hence 197 is a 
circular prime.
Example 2:

Input: N = 101
Output: 0
Explanation: 101 and 11 is prime but 110 is
not a prime number.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCircularPrime() which takes N as input parameter and returns 1 if it is Circular Prime otherwise returns 0.
 

Expected Time Complexity: O(Nlog(log(N))
Expected Space Complexity: O(N)
 

Constraints:
1 <= N <= 105
'''
#User function Template for python3
import math
class Solution:
	def isCircularPrime(self, n):
		# Code here
		def isPrime(num):
			if num <= 2:
				return False
			prime_result = [1] * (num + 1)
			prime_result[0] = 0
			prime_result[1] = 0
			for val in range(2, int(math.ceil(math.sqrt(num))) + 1):
				if prime_result[val] == 1:
					for index in range(val ** 2, num + 1, val):
						prime_result[index] = 0
			print prime_result[num]
			if prime_result[num]:
				return True
			return False

		digits = len(str(n))
		tot = digits
		temp = str(n)

		while digits > 0:
			digits = digits - 1
			if not isPrime(int(temp)):
				return False
			rem = str(int(temp) % 10)
			temp = str(int(temp) // 10)
			rem = rem + ("0" * (tot - 1))
			temp = str(int(rem) + int(temp))
			print temp

		return True

obj = Solution()
print(obj.isCircularPrime(101))		