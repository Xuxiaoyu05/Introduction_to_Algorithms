# 习题 12.3-1：给出 Tree_Insert 过程的一个递归版本。

class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None

def Tree_Insert_Recursive(root, z, y):
  if root == None:
    root = z
    if y != None:
      root.parent = y
  else:
    if z.val < root.val:
      root.left = Tree_Insert_Recursive(root.left, z, root)
    else:
      root.right = Tree_Insert_Recursive(root.right, z, root)
  
  return root
  
def Create_BinaryTree(arr):
  if len(arr) == 0:
    return None

  root = Tree(arr[0])

  if len(arr) >= 2:
    root.left = Create_BinaryTree(arr[1])
    if root.left != None:
      root.left.parent = root

  if len(arr) >= 3:
    root.right = Create_BinaryTree(arr[2])
    if root.right != None:
      root.right.parent = root
      
  return root

def PreOrder_Tree(root):
  res = []
  stack = []
  stack.append(root)

  while stack:
    cur = stack.pop()
    res.append(cur.val)
    
    if cur.right:
      stack.append(cur.right)
    if cur.left:
      stack.append(cur.left)

  return res

  
List = [12, [5, [2], [9]], [18, [15, [], [17]], [19]]]
BinaryTree = Create_BinaryTree(List)
z = Tree(13)
print(PreOrder_Tree(Tree_Insert_Recursive(BinaryTree, z, None))) 
