# 习题 12.1-3：设计一个执行中序遍历的非递归算法。（提示：一种容易的方法是使用栈作为辅助数据结构；另一种较复杂但比较简洁的做法是不使用栈，但要假设能
#              测试两个指针是否相等。）


class Tree:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

    
# 中序遍历输出的是 升序排列 的值

# 中序遍历的递归解法
def InOrder_Tree_Recursive(root):
  if root != None:
    InOrder_Tree_Recursive(root.left)
    print(root.val)
    InOrder_Tree_Recursive(root.right)

# 中序遍历的非递归解法1：使用栈
def InOrder_Tree_ByStack(root):
  if root == None:
    return None
  
  res = []
  stack = []
  cur = root
  
  while cur or len(stack) > 0:
    if cur:
      stack.append(cur)
      cur = cur.left
    else:
      cur = stack.pop()
      res.append(cur.val)
      cur = cur.right 
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

# https://www.cnblogs.com/blazebird/archive/2013/04/11/3015615.html(中序遍历的回溯解法)
# 中序遍历的非递归解法2：需要父结点指针
# 一共有三种情况：（1）访问左孩子；（2）访问右孩子；
#                （3）如果是从右孩子返回，表示整棵子树已访问完，需要沿树向上寻找父结点；直到是从左孩子返回，或者访问到根结点的父结点。

# def InOrder_Tree_Recall(root):
#   if root == None:
#     return
  
  
List = [17, [5, [2], [16]], [35, [29, [19], [33]], [37]]]
BinaryTree = Create_BinaryTree(List)
InOrder_Tree_Recursive(BinaryTree)  # 此处不要用 print，否则最后会打印出一个 None 值
print(InOrder_Tree_ByStack(BinaryTree))
# InOrder_Tree_Recall(BinaryTree)
