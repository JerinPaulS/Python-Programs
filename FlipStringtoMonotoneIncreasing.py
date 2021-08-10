'''
Flip String to Monotone Increasing
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
'''
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        ones_left = [0] * size
        zero_right = [0] * size

        for index in range(1, size):
        	if s[index - 1] == "1":
        		zero_right[index] = 1 + zero_right[index - 1]
        	else:
        		zero_right[index] = zero_right[index - 1]

        for index in range(size - 2, -1, -1):
        	if s[index + 1] == "0":
        		ones_left[index] = 1 + ones_left[index + 1]
        	else:
        		ones_left[index] = ones_left[index + 1]

        result = size
        for index in range(size):
        	result = min(result, zero_right[index] + ones_left[index])

        print ones_left, zero_right
        return result

obj = Solution()
print(obj.minFlipsMonoIncr("00110"))