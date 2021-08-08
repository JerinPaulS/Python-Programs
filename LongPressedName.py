'''
925. Long Pressed Name
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
name and typed contain only lowercase English letters.
'''
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        ptr1 = 0
        ptr2 = 0
        size1 = len(name)
        size2 = len(typed)
        if size1 > size2:
            return False
        if size1 == size2 and name != typed:
            return False
        while ptr2 < size2:
        	if ptr1 < size1 and name[ptr1] == typed[ptr2]:
        		ptr1 = ptr1 + 1
        	elif ptr2 == 0 or typed[ptr2] != typed[ptr2 - 1]:
        		return False
        	ptr2 = ptr2 + 1
    	return ptr1 == size1

obj = Solution()
print(obj.isLongPressedName(name = "alex", typed = "aaleex"), "true")
print(obj.isLongPressedName(name = "saeed", typed = "ssaaedd"), "flase")
print(obj.isLongPressedName(name = "leelee", typed = "lleeelee"), "true")
print(obj.isLongPressedName(name = "laiden", typed = "laiden"), "true")