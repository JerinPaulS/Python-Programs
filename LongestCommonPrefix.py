'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = 9999
        min_word = ""
        index = 0
        for i in range(len(strs)):
        	if len(strs[i]) < min_len:
        		min_len = len(strs[i])
        		min_word = strs[i]
        		index = i

        for i in range(0, len(strs)):
        	if min_word == "":
        		break
        	if index != i:
	        	for j in range(0, len(min_word)):
	        		if strs[i][j] != min_word[j]:
	        			min_word = min_word[:j]
	        			break
        				
        print(min_word)

obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])