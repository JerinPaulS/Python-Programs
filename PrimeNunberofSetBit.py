'''
762. Prime Number of Set Bits in Binary Representation
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101 which has 3 set bits.
 

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
 

Constraints:

1 <= left <= right <= 106
0 <= right - left <= 104
'''
import math
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_nos = [2, 3, 5, 7, 11, 13, 17, 19] # since the upper bound is 10^6 -> max number of set bit = log(10^6, 2) ~= 20

        def count_setBits(num):
        	count = 0
        	while num:
        		num = num & (num - 1)
        		count = count + 1
        	return count

        result = 0
        for val in range(left, right + 1):
        	if count_setBits(val) in prime_nos:
        		result = result + 1

        return result


obj = Solution()
print(obj.countPrimeSetBits(left = 6, right = 10))
print(obj.countPrimeSetBits(left = 10, right = 15))

'''
		prime_nos = [1] * (right + 1)
        set_bits = [0] * (right + 1)
        set_bits[1] = 1
        offset = 1
        for index in range(2, right + 1):
        	if offset * 2 == index:
        		offset = index
        	set_bits[index] = 1 + set_bits[index - offset]

        for num in range(2, int(math.ceil(math.sqrt(right)) + 1)):
        	if prime_nos[num] == 1:
        		for index in range(num ** 2, right + 1, num):
        			prime_nos[index] = 0

        prime_nos[0] = 0
        prime_nos[1] = 0

        result = 0
        for index in range(left, right + 1):
        	if prime_nos[set_bits[index]] == 1:
        		result = result + 1

        return result
'''      