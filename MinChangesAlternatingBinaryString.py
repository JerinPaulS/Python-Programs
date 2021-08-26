'''
1758. Minimum Changes To Make Alternating Binary String
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
'''
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        even = [0, 0]
        odd = [0, 0]
        index = 0
        result = 0
        size = len(s) // 2
        for char in s:
        	if index % 2 == 0:
        		if char == "1":
        			even[0] = even[0] + 1
        		else:
        			even[1] = even[1] + 1
        	else:        		
        		if char == "1":
        			odd[0] = odd[0] + 1
        		else:
        			odd[1] = odd[1] + 1
        	index = index + 1
        result = min(even[0] + odd[1], even[1] + odd[0])
        return result

obj = Solution()
print(obj.minOperations("01001"))