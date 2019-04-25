# 习题 12.1-4：对于一棵有 n 个结点的树，请设计在 θ(n) 时间内完成的先序遍历算法和后续遍历算法。

# 后序遍历

class Tree:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


# 后序遍历的递归解法
def PostOrder_Tree_Recursive(root):
  if root != None:
    PostOrder_Tree_Recursive(root.left)
    PostOrder_Tree_Recursive(root.right)
    print(root.val)

# 后序遍历的非递归解法
def PostOrder_Tree_ByStack_Recall(root):
  if root == None:
    return
  
  res = []
  stack = []
  stack.append(root)
  
  cur = None
  pre = None  # 记录上一次返回的结点
  
  while stack:
    cur = stack[-1]
    # 只要满足：（1）是叶子结点；（2）是回溯的。其中之一，则回溯
    if cur.left == cur.right == None or (pre == cur.left or pre == cur.right):
      res.append(cur.val)
      stack.pop()
      pre = cur
    # 如果不满足上述两个条件，继续按照先右后左（因为栈是后进先出）的顺序向栈中插入值
    else:
      if cur.right:
        stack.append(cur.right)
      if cur.left:
        stack.append(cur.left)
        
  return res

def Create_BinaryTree(arr):
  if len(arr) == 0:
    return
  root = Tree(arr[0])
  if len(arr) >= 2:
    root.left = Create_BinaryTree(arr[1])
  if len(arr) >= 3:
    root.right = Create_BinaryTree(arr[2])
  
  return root

List = [17, [5, [2], [16]], [35, [29, [19], [33]], [37]]]
BinaryTree = Create_BinaryTree(List)
PostOrder_Tree_Recursive(BinaryTree)
print(PostOrder_Tree_ByStack_Recall(BinaryTree))
