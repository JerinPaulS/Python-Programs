'''
Easy Sum Set Problem
Problem
In this problem, we define "set" is a collection of distinct numbers. For two sets  and , we define their sum set is a set . In other word,  set  contains all elements which can be represented as sum of an element in  and an element in . Given two sets , your task is to find set  of positive integers less than or equals  with maximum size such that . It is guaranteed that there is unique such set.

Input Format

The first line contains  denoting the number of elements in set , the following line contains  space-separated integers  denoting the elements of set .

The third line contains  denoting the number of elements in set , the following line contains  space-separated integers  denoting the elements of set .

Output Format

Print all elements of  in increasing order in a single line, separated by space.

Constraints

 

Sample Input
2
1 2
3
3 4 5

Sample Output
2 3
Time Limit: 2
Memory Limit: 256
Source Limit:
Explanation
If  is an element of set , then  is an element of set , so we must have . Clearly,  cannot be  because  is not an element of set . Therefore, .
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import collections
N = int(input())
A = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
result = []
res = []
for i in range(N):
    for j in range(M):
        res.append(C[j] - A[i])    

res = collections.Counter(res)
for key, val in res.items():
    if val == N:
        result.append(key)
result = sorted(result)
print(' '.join(map(str, result)))