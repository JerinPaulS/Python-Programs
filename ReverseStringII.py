'''
541. Reverse String II
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
'''
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = list(s)
        start = 0
        end = min(start + k - 1, len(s) - 1)
        while start < len(s):
        	temp_start = start
        	temp_end = end
        	while temp_start <= temp_end:
        		temp_val = s_list[temp_start]
        		s_list[temp_start] = s_list[temp_end]
        		s_list[temp_end] = temp_val
        		temp_start = temp_start + 1
        		temp_end = temp_end - 1
        	start = start + (2 * k)
        	end = min(start + k - 1, len(s) - 1)

        s = ''.join(s_list)
        return s

obj = Solution()
print(obj.reverseStr(s = "abcdefg", k = 2))
print(obj.reverseStr(s = "abcd", k = 2))
print(obj.reverseStr(s = "abc", k = 2))