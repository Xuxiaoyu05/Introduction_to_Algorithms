# 习题 12.3-6：当 Tree_Delete 中的结点 z 有两个孩子时，应选择结点 y 作为它的前驱，而不是作为它的后继。如果这样做，对 Tree_Delete 应该做些什么必要的修改？
#              一些人提出了一个公平策略，为前驱和后继赋予相等的优先级，这样得到了较好的实验性能。如何对 Tree_Delete 进行修改来实现这样一种公平策略？

import random

class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    
def Transplant(root, u, v):
  if u.parent == None: 
    root = v
  else:
    if u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
  
  if v != None:
    v.parent = u.parent

def Maximum(root):
  while root.right:
    root = root.right
  return root

def Minimum(root):
  while root.left:
    root = root.left
  return root
  
def Tree_Delete_Predecessor(root, z):
  if z.left == None:
    Transplant(root, z, z.right)
  elif z.right == None:
    Transplant(root, z, z.left)
  else:
    y = Maximum(z.left)
    if y.parent != z:
      Transplant(root, y, y.left)
      y.left = z.left
      y.left.parent = y
      
    Transplant(root, z, y)
    y.right = z.right
    y.right.parent = y
  
  return root

# 公平选择用前驱或后继来替换待删除结点
def Tree_Delete_Mixed(root, z):
  if z.left == None:
    Transplant(root, z, z.right)
  elif z.right == None:
    Transplant(root, z, z.left)
  else:
    if random.randint(1, 2) == 1:  # 采用后继来替换待删除结点
      y = Minimum(z.right)
      if y.parent != z:
        Transplant(root, y, y.right)
        y.right = z.right
        y.right.parent = y
      
      Transplant(root, z, y)
      y.left = z.left
      y.left.parent = y
    
    else:  # 采用前驱来替换待删除结点
      
      y = Maximum(z.left)
      if y.parent != z:
        Transplant(root, y, y.left)
        y.left = z.left
        y.left.parent = y
      
      Transplant(root, z, y)
      y.right = z.right
      y.right.parent = y
    
  return root


def Create_BinaryTree(arr):
  if len(arr) == 0:
     return
     
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
z = BinaryTree.right
# print(PreOrder_Tree(Tree_Delete_Predecessor(BinaryTree, z)))
print(PreOrder_Tree(Tree_Delete_Mixed(BinaryTree, z)))
