'''
744. Find Smallest Letter Greater Than Target
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"
 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters) - 1
        while start <= end:
        	mid = (start + end) // 2
        	if letters[mid] > target:
        		end = mid - 1
        	else:
        		start = mid + 1

        if start > len(letters) - 1:
        	return letters[0]
        else:
        	return letters[start]

obj = Solution()
print(obj.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(obj.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(obj.nextGreatestLetter(letters = ["c","f","j"], target = "d"))
print(obj.nextGreatestLetter(letters = ["c","f","j"], target = "g"))
print(obj.nextGreatestLetter(letters = ["c","f","j"], target = "j"))
print(obj.nextGreatestLetter(letters = ["a","b","c"], target = "z"))