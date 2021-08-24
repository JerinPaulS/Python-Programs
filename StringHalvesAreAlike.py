'''
1704. Determine if String Halves Are Alike
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
'''
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        a = s[:size // 2]
        b = s[size // 2:size]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a_count = 0
        b_count = 0

        for index in range(len(a)):
        	if a[index] in vowels:
        		a_count = a_count + 1
        for index in range(len(b)):
        	if b[index] in vowels:
        		b_count = b_count + 1

        return a_count == b_count