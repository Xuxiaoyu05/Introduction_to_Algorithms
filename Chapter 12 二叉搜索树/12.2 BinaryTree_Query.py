# 查询：查找一个存储在二叉搜索树中的关键字。

# 查询操作：（1）Search；（2）Minimum；（3）Maximum；（4）Successor；（5）Predecessor。时间复杂度均为 O(n)。
# 定理：在一棵高度为 h 的二叉搜索树上，动态集合上的操作 Search、Minimum、Maximum、Successor、Predecessor 可以在 O(h) 时间内完成。

class Tree:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    self.parent = None


# （1）Search：在一棵二叉搜索树中查找一个具有给定关键字的结点
# 输入：一个指向树根的指针和一个关键字 k
# 输出：一个指向关键字为 k 的结点的指针，否则返回 None
# 该过程从树根开始查找，并沿着这棵树中的一条简单路径向下进行，运行时间为 O(h)，h 为树的高度。

# 查找的递归写法
def Tree_Search_Recursive(root, k):
  if root == None or root.val == k:
    return root
  if root.val < k:
    return Tree_Search_Recursive(root.right, k)
  else:
    return Tree_Search_Recursive(root.left, k)

# 查找的循环写法
def Tree_Search_Iterative(root, k): 
  while root != None and k != root.val:
    if root.val < k:
      root = root.right
    else:
      root = root.left
  return root


 
#（2）Minimum：最小关键字
# 从树根开始一直沿着 left 指针直到遇到 None
# 依据原理：以 root 为根的子树中的最小关键字一定在以 root.left 为根的子树中。
# 该过程从树根开始查找，并沿着这棵树中的一条简单路径向下进行，运行时间为 O(h)，h 为树的高度。
def Minimum(root):
  if root == None:
    return None
    
  while root.left:
    root = root.left
    
  return root
  
  
#（3）Maximum：最大关键字
# 从树根开始一直沿着 right 指针直到遇到 None
# 依据原理：以 root 为根的子树中的最大关键字一定在以 root.right 为根的子树中。 
# 该过程从树根开始查找，并沿着这棵树中的一条简单路径向下进行，运行时间为 O(h)，h 为树的高度。
def Maximum(root):
  if root == None:
    return None
    
  while root.right:
    root = root.right
    
  return root


#（4）Successor：后继
# 给定一棵二叉搜索树中的一个结点，按中序遍历的次序查找它的后继。
# 如果所有的关键字各不相同，则一个结点 x 的后继是大于 x.key 的最小关键字的结点。如果 x 是这棵树值中的最大关键字，返回 None。
# 分两种情况：（1）如果 x 的右子树非空，则 x 的后继是 x 右子树中的最小关键字
#            （2）如果 x 的右子树为空且有一个后继 y，那么 y 是 x 的最底层祖先，且 y 的左孩子也是 x 的一个祖先。
#                 即从 x 开始沿树向上直到遇到这样一个结点，这个结点是它双亲的左孩子。
# 该过程遵循一条简单路径沿树向上或遵循简单路径沿树向下，运行时间为 O(h)，h 为树的高度。

def Successor(x):
  if x == None:
    return None
  
  if x.right:
    return Minimum(x.right)
  
  y = x.parent
  while y != None and x == y.right:
    x = y
    y = x.parent
    
  return y


#（5）Predecessor：前驱
# 如果所有的关键字各不相同，则一个结点 x 的前驱是小于 x.key 的最大关键字的结点。如果 x 是这棵树值中的最小关键字，返回 None。
# 分两种情况：（1）若 x 的左子树不为空，则 x 的前驱是 x 左子树中的最大关键字
#            （2）若 x 的左子树为空且有一个前驱y，则 y 是 x 的最底层祖先，且 y 的右孩子也是 x 的一个祖先。
#                 即从 x 开始沿树向上直到遇到这样一个结点，这个结点是它双亲的右孩子。

def Predecessor(x):
  if x == None:
    return None
    
  if x.left:
    return Maximum(x.left)
  
  y = x.parent
  while y != None and x == y.left:
    x = y
    y = x.parent
  
  return y
  

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
 
List = [15, [6, [3, [2], [4]], [7, [], [13, [9], []]]], [18, [17], [20]]]
BinaryTree = Create_BinaryTree(List)
print(Tree_Search_Recursive(BinaryTree, 13).val) 
print(Tree_Search_Iterative(BinaryTree, 18).val)
print(Minimum(BinaryTree).val) 
print(Maximum(BinaryTree).val)
print(Successor(Tree_Search_Iterative(BinaryTree, 15)).val)  # 15 的后继是 17
print(Successor(Tree_Search_Iterative(BinaryTree, 13)).val)  # 13 的后继是 15
print(Predecessor(Tree_Search_Iterative(BinaryTree, 7)).val) # 7 的前驱是 6
print(Predecessor(Tree_Search_Iterative(BinaryTree, 17)).val) # 17 的前驱是 15
