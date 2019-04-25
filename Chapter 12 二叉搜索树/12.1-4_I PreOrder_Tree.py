# 习题 12.1-4：对于一棵有 n 个结点的树，请设计在 θ(n) 时间内完成的先序遍历算法和后续遍历算法。

# 先序遍历

class Tree:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    
# 先序遍历的递归解法
def PreOrder_Tree_Recursive(root):
  if root != None:
    print(root.val)
    PreOrder_Tree_Recursive(root.left)
    PreOrder_Tree_Recursive(root.right)

# 先序遍历的非递归解法
def PreOrder_Tree_ByStack(root):
  if root == None:
    return
  
  stack = []
  res = []
  stack.append(root)
  
  while stack:
    cur = stack.pop()
    res.append(cur.val)
    
    if cur.right:
      stack.append(cur.right)

    if cur.left:
      stack.append(cur.left)
    
  return res
  
def Create_BinaryTree(arr):
  if len(arr) == 0:
    return None
  
  root = Tree(arr[0])
  
  if len(arr) >= 2:
    root.left = Create_BinaryTree(arr[1])
  if len(arr) >= 3:
    root.right = Create_BinaryTree(arr[2])
  
  return root

List = [17, [5, [2], [16]], [35, [29, [19], [33]], [37]]]
BinaryTree = Create_BinaryTree(List)
PreOrder_Tree_Recursive(BinaryTree)
print(PreOrder_Tree_ByStack(BinaryTree))
