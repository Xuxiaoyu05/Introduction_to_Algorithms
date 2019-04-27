# 二叉搜索树的删除

# 从二叉搜索树 T 中删除一个结点 z 可分为三种情况：
#（1）如果 z 没有孩子结点，直接将其删除，并修改它的父结点，用 None 作为孩子来替换 z
#（2）如果 z 只有一个孩子，那么将这个孩子提升到树中 z 的位置上，并修改 z 的父结点，用 z 的孩子来替换 z
#（3）如果 z 有两个孩子，那么找 z 的后继 y（一定在 z 的右子树中），并让 y 占据树中 z 的位置。z 的原来右子树部分称为 y 的新的右子树，并且 z 的左子树
#     成为 y 的新的左子树，这种情况略微麻烦，因为还与 y 是否为 z 的右孩子相关。

# 代码实现过程：
#（1）如果 z 没有左孩子，那么用其右孩子来替换 z，右孩子可以是 None 或不是。当 z 的右孩子也为 None 的时候，这种情况归为 z 没有孩子结点的情形；
#     当右孩子非 None 的时候，这种情况就是 z 只有一个孩子结点且该孩子为右孩子的情形；
#（2）如果 z 仅有一个孩子且为左孩子，那么用其左孩子来替换 z；
#（3）否则，z 既有一个左孩子又有一个右孩子。我们需要查找 z 的后继 y，这个后继位于右子树中且没有左孩子（见习题12.2-5）。
#     现在需要将 y 移出原来的位置替换树中的 z。
#     A. 如果 y 是 z 的右孩子，那么用 y 替换 z，并仅留下 y 的右孩子；
#     B. 否则 y 位于 z 的右子树中但并不是 z 的右孩子，在这种去情况下，先用 y 的右孩子替换 y，再用 y 替换 z。


class Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None

def Minimum(root):
  while root.left:
    root = root.left
  return root

# 定义子过程 Transplant：用另一棵子树替换一棵子树并成为其双亲的孩子结点。
# 当 Transplant 用一棵以 v 为根的子树来替换一棵以 u 为根的子树时，结点 u 的双亲就变为结点 v 的双亲，且 v 成为 u 的双亲的相应孩子。

def Transplant(root, u, v):
  if u.parent == None: # 只有树根结点的父结点为 None
    root = v
  else:
    if u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
  
  if v != None:
    v.parent = u.parent

# 除了调用 Minimum 之外，Tree_Delete 的每一行，包括调用 Transplant，都只花费常数时间。
# 在一棵高度为 h 的树上，Tree_Delete 的运行时间为 O(h)

def Tree_Delete(root, z):
  if z.left == None:
     Transplant(root, z, z.right)
  elif z.right == None:
    Transplant(root, z, z.left)
  else:
    y = Minimum(z.right)
    if y.parent != z:
      Transplant(root, y, y.right)
      y.right = z.right
      y.right.parent = y  # 此处是 y.right
    
    Transplant(root, z, y)
    y.left = z.left
    y.left.parent = y
  
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
print(PreOrder_Tree(Tree_Delete(BinaryTree, z)))

# 定理：在一棵高度为 h 的二叉搜索树上，实现动态集合操作 Insert 和 Delete 的运行时间为 O(h)。
