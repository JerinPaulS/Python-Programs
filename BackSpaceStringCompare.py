'''
844. Backspace String Compare
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?


'''
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def removeHash(string):
        	result = ""
        	count = 0
        	for index, char in enumerate(string[::-1]):
        		if char == "#":
        			count = count + 1
        		if count > 0 and char != "#":
        			count = count - 1
        			continue
        		elif char != "#" and count == 0:
        			result = char + result
        	return result

        s_update = removeHash(s)
        t_update = removeHash(t)
        return s_update == t_update


"xywrrmp"
"xywrrmu#p"     
