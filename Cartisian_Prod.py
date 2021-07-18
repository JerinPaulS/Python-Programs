'''
Task

You are given a two lists  and . Your task is to compute their cartesian product X.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list .
The second line contains the space separated elements of list .

Both lists have no duplicate integer elements.

Constraints



Output Format

Output the space separated tuples of the cartesian product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
'''
from itertools import product
A = raw_input().split()
B = raw_input().split()
for i in range(len(A)):
	A[i] = int(A[i])
for i in range(len(B)):
	B[i] = int(B[i])

result = list(product(A, B))
for i in range(len(result)):
	print(result[i]),