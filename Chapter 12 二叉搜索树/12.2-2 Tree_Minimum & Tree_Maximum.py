# 习题 12.2-2：写出 Tree_Minimum 和 Tree_Maximum 的递归版本。

class Tree:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    
def Tree_Minimum_Recursive(root):
  if root.left:
    return Tree_Minimum_Recursive(root.left)
  else:
    return root
  
def Tree_Maximum_Recursive(root):
  if root.right:
    return Tree_Maximum_Recursive(root.right)
  else:
    return root
 
def Create_BinaryTree(arr):
  if len(arr) == 0:
    return
    
  root = Tree(arr[0])
  
  if len(arr) >= 2:
    root.left = Create_BinaryTree(arr[1])
  
  if len(arr) >= 3:
    root.right = Create_BinaryTree(arr[2])
  
  return root
  
List = [15, [6, [3, [2], [4]], [7, [], [13, [9], []]]], [18, [17], [20]]]
BinaryTree = Create_BinaryTree(List)
print(Tree_Minimum_Recursive(BinaryTree).val)
print(Tree_Maximum_Recursive(BinaryTree).val)
