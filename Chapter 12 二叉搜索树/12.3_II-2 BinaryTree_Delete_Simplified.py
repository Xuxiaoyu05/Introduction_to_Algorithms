# 二叉搜索树删除结点的简化版（无父结点）

# 结点删除也分为三种情况：
#（1）待删除结点既无左子树也无右子树：直接删除该结点即可；
#（2）待删除结点只有左子树或只有右子树：将其左子树或右子树根结点代替待删除结点；
#（3）待删除结点既有左子树又有右子树：找到该结点的后继结点（右子树中），使用该结点代替待删除结点，然后递归在右子树中删除该后继结点。

class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
def Minimum(x):
  while x.left:
    x = x.left
  return x
 
def Tree_Delete_Simplified(root, val):
  if root == None:
    return

  if val < root.val:
    root.left = Tree_Delete_Simplified(root.left, val)
  elif val > root.val:
    root.right = Tree_Delete_Simplified(root.right, val)
  else: # 分三种情况：（1）只有左子树（2）只有右子树（3）既有左子树又有右子树
    if root.left == None and root.right == None:
      root = None
    elif root.left == None:
      root = root.right
    elif root.right == None:
      root = root.left
    else:
      temp = Minimum(root.right)
      root.val = temp.val
      root.right = Tree_Delete_Simplified(root.right, temp.val)

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
val = 18
print(PreOrder_Tree(Tree_Delete_Simplified(BinaryTree, val))) 
