'''
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
        	return False
        target = collections.Counter(s1)
        length = len(s1)
        index = 0
        while index < length:
        	if target.has_key(s2[index]):
        		target[s2[index]] = target[s2[index]] - 1
        	index = index + 1
        values = target.values()
        if values.count(0) == len(values):
        	return True
        for index in range(length, len(s2)):        	
        	if target.has_key(s2[index - length]):
        		target[s2[index - length]] = target[s2[index - length]] + 1
        	if target.has_key(s2[index]):
        		target[s2[index]] = target[s2[index]] - 1
        	values = target.values()
        	print s2[index - 1], s2[index], target
        	if values.count(0) == len(values):
        		return True
        print target
        return False

obj = Solution()
print(obj.checkInclusion(s1 = "ab", s2 = "eidbaooo"))        