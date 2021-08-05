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
		ptr1 = len(s) - 1
        ptr2 = len(t) - 1

        def getNextValidCharIndex(string, index):
            count = 0
            while index >= 0:
                if string[index] == "#":     
                    count = count + 1
                elif count > 0:           
                    count = count - 1
                else:
                    break
                index = index - 1
            return index


        while ptr1 >= 0 or ptr2 >= 0:
            nptr1 = getNextValidCharIndex(s, ptr1)
            nptr2 = getNextValidCharIndex(t, ptr2)
            if nptr1 < 0 and nptr2 < 0:
                return True
            if nptr1 < 0 or nptr2 < 0:
                return False
            if s[nptr1] != t[nptr2]:
                return False
            ptr1 = nptr1 - 1
            ptr2 = nptr2 - 1
        return True
    
obj = Solution()
#print(obj.backspaceCompare("bxj##tw","bxo#j##tw"))
print(obj.backspaceCompare("bxj##tw","bxj###tw"))
#print(obj.backspaceCompare("a##c","#a#c"))
