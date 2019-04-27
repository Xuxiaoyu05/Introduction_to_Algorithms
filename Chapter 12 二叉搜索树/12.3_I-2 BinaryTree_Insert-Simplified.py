# 向二叉树中插入结点简化版：无需父结点，用递归的方式

class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
def Tree_Insert_Simplified(root, z):
  if root == None:
    return z
  
  if z.val < root.val:
    root.left = Tree_Insert_Simplified(root.left, z)  # 注意这个地方是 root.left = ...
  else:
    root.right = Tree_Insert_Simplified(root.right, z)
  
  return root


def Create_BinaryTree(arr):
  if len(arr) == 0:
    return None
    
  root = Tree(arr[0])
  
  if len(arr) >= 2:
    root.left = Create_BinaryTree(arr[1])

  if len(arr) >= 3:
    root.right = Create_BinaryTree(arr[2])

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
print(PreOrder_Tree(Tree_Insert_Simplified(BinaryTree, z))) 
