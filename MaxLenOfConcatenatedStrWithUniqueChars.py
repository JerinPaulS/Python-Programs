'''
Maximum Length of a Concatenated String with Unique Characters
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        result = [0]
        def has_dup(s):
        	return len(s) == len(set(s))

        def backtrack(index, curr):
        	result[0] = max(result[0], len(curr))

        	for i in range(index, len(arr)):
        		new_s = curr + arr[i]
        		if has_dup(new_s):
        			backtrack(i + 1, new_s)

        	return

        backtrack(0, "")
        return result[0]