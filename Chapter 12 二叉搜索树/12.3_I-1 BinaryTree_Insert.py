# 二叉搜索树的插入与删除

# 目的：保证二叉搜索树性质的成立。

class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    
# 插入
# 输入：根结点 T，结点 z, 其中 z.key = v，z.left = None, z.right = None。
# 这个过程要修改 T 和 z 的某些属性，来把 z 插入到树中的相应位置上。
# 过程 Tree_Insert 在一棵高度为 h 的树上的运行时间为 O(h)
def Tree_Insert(root, z):
  y = None
  x = root
  
  # 查找 z 要替换的 None（搜索 z 的位置）
  # y 是 x 的双亲
  while x != None:
    y = x
    if z.val < x.val:
      x = x.left
    else:
      x = x.right
  
  z.parent = y
  if y == None: # 树为空树
    root = y
  else:
    if z.val < y.val:
      y.left = z
    else:
      y.right = z
  
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
print(PreOrder_Tree(Tree_Insert(BinaryTree, z))) 
