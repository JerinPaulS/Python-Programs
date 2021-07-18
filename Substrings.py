'''
itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
inp = input().split()
inp_str = inp[0]
word = list()
for i in range(len(inp_str)):
    word.append(inp_str[i])

leng = int(inp[1])
substring = list()
i = 1
while i <= leng:
    substring.append(list(combinations(word, i)))
    i = i + 1

final = list()
temp = ""

for i in range(len(substring)):
    for j in range(len(substring[i])):
        for k in range(len(substring[i][j])):
            if(substring[i][j][k].isalpha()):
                temp = temp + substring[i][j][k].upper()
        final.append(str(sorted(temp)))
        temp = ""

final.sort()

i = 1
while i <= leng:
    for j in range(len(final)):
        if(len(final[j]) == i):
            print(final[j])
    i = i + 1
    
