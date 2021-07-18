'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or len(s) < 1 or len(t) < 1:
        	return False
        dict = {}
        for index in range(len(s)):
        	if dict.has_key(s[index]):
        		if dict[s[index]] != t[index]:
        			return False
        	if t[index] in dict.values():
        		key_list = dict.keys()
        		val_list = dict.values()
        		if key_list[val_list.index(t[index])] != s[index]:
        			return False
        	else:
        		dict[s[index]] = t[index]

        return True

obj = Solution()
print(obj.isIsomorphic(s = "egg", t = "add"))
print(obj.isIsomorphic("badc","baba"))
print(obj.isIsomorphic(s = "paper", t = "title"))