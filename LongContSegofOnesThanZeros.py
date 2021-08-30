'''
1869. Longer Contiguous Segments of Ones than Zeros
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.

 

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
 

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
'''
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_length_1 = float('-inf')
        max_length_0 = float('-inf')
		curr_length_1 = 0
		curr_length_0 = 0

		for index in range(len(s)):
			if (s[index] == '1'):
				curr_length_1 = curr_length_1 + 1
				max_length_1 = max(curr_length_1, max_length_1)
				curr_length_0 = 0

			if (s[index] == '0'):
				curr_length_0 = curr_length_0 + 1
				max_length_0 = max(curr_length_0, max_length_0)
				curr_length_1 = 0

		return max_length_1 > max_length_0