'''
1624. Largest Substring Between Two Equal Characters
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".
 

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
'''
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        for_dict = {}
        bac_dict = {}
        size = len(s)
        for index in range(size):
        	if for_dict.has_key(s[index]):
        		continue
        	else:
        		for_dict[s[index]] = index
        for index in range(size - 1, -1, -1):
        	if bac_dict.has_key(s[index]):
        		continue
        	else:
        		bac_dict[s[index]] = index

        result = -1
        for key in for_dict.keys():
        	result = max(result, bac_dict[key] - for_dict[key] - 1)

        return result