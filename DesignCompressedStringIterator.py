'''
LeetCode 604 - Design Compressed String Iterator
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.
The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.
next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.
Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.
Example:
StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
'''
class Solution(object):
	def __init__(self, compressedString):
		self.alphabet = ""
		self.count = 0
		self.whole_string = ""
		self.current_ptr = -1
		for char in compressedString:
			if char.isalpha():				
				if self.count > 0:
					self.whole_string = self.whole_string + (self.alphabet * self.count)
				self.alphabet = char
				self.count = 0
			elif char.isdigit():
				self.count = (self.count * 10) + int(char)
		self.whole_string = self.whole_string + (self.alphabet * self.count)

	def next(self):
		self.current_ptr = self.current_ptr + 1
		if self.current_ptr == len(self.whole_string):
			return " "
		else:
			return self.whole_string[self.current_ptr]

	def hasNext(self):
		if self.current_ptr >= len(self.whole_string) - 1:
			return False
		else:
			return True
"""
 # Your StringIterator object will be instantiated and called as such:
 # StringIterator obj = new StringIterator(compressedString);
 # char param_1 = obj.Next();
 # bool param_2 = obj.HasNext();
"""
obj = Solution("L1e2t1C1o1d1e1")
print(obj.next())# return 'L'
print(obj.next())# return 'e'
print(obj.next())# return 'e'
print(obj.next())# return 't'
print(obj.next())# return 'C'
print(obj.next())# return 'o'
print(obj.next())# return 'd'
print(obj.hasNext())# return true
print(obj.next())# return 'e'
print(obj.hasNext())# return false
print(obj.next())# return ' '