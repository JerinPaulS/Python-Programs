'''
1941. Check if All Characters Have Equal Number of Occurrences
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''
import collections
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_freq = collections.Counter(s)
        keys = char_freq.keys()
        size = len(keys)
        target = char_freq[keys[0]]
        for index in range(1, size):
        	if target == char_freq[keys[index]]:
        		pass
        	else:
        		return False

        return True



obj = Solution()
print(obj.areOccurrencesEqual("aaabb"))        