'''
 346 Moving Average from Data Stream
Description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
'''

from collections import deque
import decimal
class MovingAverage:
	"""
	@param: size: An integer
	"""


	def __init__(self, size):
		# do intialization if necessary
		self.maxsize = size
		self.que = deque()
		self.result = 0.0

		"""
		@param: val: An integer
		@return:  
		"""
	def next(self, val):
		# write your code here
		if len(self.que) == self.maxsize:
			self.que.popleft()
		self.que.append(val)
		self.result = float(decimal.Decimal(sum(self.que)) / decimal.Decimal(len(self.que)))
		return("{0:.5f}".format(self.result))


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param = obj.next(1)
print param
param = obj.next(10)
print param
param = obj.next(3)
print param
param = obj.next(5)
print param