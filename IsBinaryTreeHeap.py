'''
Is Binary Tree Heap
Given a binary tree you need to check if it follows max heap property or not.

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part which stores the data, pointer to left child and pointer to right child.There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return true if property holds else false.
 

Example 1:

Input:
      5
    /  \
   2    3
Output: 1
Example 2:

Input:
       10
     /   \
    20   30 
  /   \
 40   60
Output: 0
Constraints:
1 ≤ Number of nodes ≤ 100
1 ≤ Data of a node ≤ 1000


'''
#User Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        def count_nodes(self, root):
        if root is None:
            return 0
        else:
            return (1 + self.count_nodes(root.left) + self.count_nodes(root.right))
 
    def heap_propert_util(self, root):
 
        if (root.left is None and root.right is None):
            return True
 
        if root.right is None:
            return root.data >= root.left.data
        else:
            if (root.data >= root.left.data and root.data >= root.right.data):
                return (self.heap_propert_util(root.left) and self.heap_propert_util(root.right))
            else:
                return False
 
    def complete_tree_util(self, root, index, node_count):
        if root is None:
            return True
        if index >= node_count:
            return False
        return (self.complete_tree_util(root.left, 2 * index + 1, node_count) and self.complete_tree_util(root.right, 2 * index + 2, node_count))
 
    def isHeap(self, root):
        node_count = self.count_nodes(root)
        if (self.complete_tree_util(root, 0, node_count) and self.heap_propert_util(root)):
            return True
        else:
            return False
'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Susanta Mukherjee
import sys
sys.setrecursionlimit(10**6)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        ob = Solution()
        if ob.isHeap(root):
            print(1)
        else:
            print(0)
        
        

# } Driver Code Ends
'''