'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
Example 4:

Input: columnTitle = "FXSHRXW"
Output: 2147483647
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
'''
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        count = 0
        for char in columnTitle:
        	count = count + 1
        	if char == columnTitle[len(columnTitle) - 1] and count == len(columnTitle):
        		result = result + ((ord(char) + 1) % 65)
        	else:
        		result = result + (((ord(char) + 1) % 65) * 26 ** (len(columnTitle) - count))        
        return result

obj = Solution()
print(obj.titleToNumber("AA"))
print(obj.titleToNumber("AB"))
print(obj.titleToNumber("ZY"))
print(obj.titleToNumber("FXSHRXW"))