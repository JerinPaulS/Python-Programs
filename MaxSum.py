'''
Maximum Sum
Problem
You are given an array of integers , you need to find the maximum sum that can be obtained by picking some non-empty subset of the array. If there are many such non-empty subsets, choose the one with the maximum number of elements. Print the maximum sum and the number of elements in the chosen subset.

Input:

The first line contains an integer , denoting the number of elements of the array. Next line contains  space-separated integers, denoting the elements of the array.

Output:

Print  space-separated integers, the maximum sum that can be obtained by choosing some subset and the maximum number of elements among all such subsets which have the same maximum sum.

Constraints:

Sample Input
5
1 2 -4 -2 3
Sample Output
6 3
Time Limit: 1
Memory Limit: 256
Source Limit:
Explanation
The chosen subset is {1, 2, 3}.
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
size = int(input())
nums = input().split(' ')

count = 0
result = 0
min_element = -float('inf')

for num in nums:
	if int(num) >= 0:
		count = count + 1
		result = result + int(num)
	if int(num) < 0:
		min_element = max(min_element, int(num))
if result <= 0:
	if min_element == -float('inf'):
		min_element = 0
	result = min_element
	count = 1
print(str(result) + " " + str(count))