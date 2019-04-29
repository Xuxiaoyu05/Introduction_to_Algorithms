# 向红黑树中插入新结点

# 基本思想：(1) 利用 Tree_Insert 的略修改版本 RB_Treee_Insert 将新结点 z 插入树 T 内（将树 T 视为一棵普通的二叉搜索树），然后将 z 着为红色（不能是黑色）；
#          (2) 为了保证红黑性质，调用辅助过程 RB_Insert_Fixup 来对结点进行重新着色并旋转。

# 时间复杂度 O(lgn)

# RB_Insert_Fixup 过程（三步骤）：
# 分析：当新结点 z 被插入并着为红色，可能被破坏的红黑性质。

class RB_Tree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    self.color = "BLACK"


def RB_Tree_Insert_Fixup(root, z):
  




def RB_Tree_Insert(root, z):
  y = None
  x = root
  
  while x != None:
    y = x
    if z.val < x.val:
      x = x.left
    else:
      x = x.right
  
  z.parent = y
  if y == None:
    root = z
  else:
    if z.val < y.val:
      y.left = z
    else:
      y.right = z
  
  # z.left = None
  # z.right = None
  
  z.color = "RED"   # 将 z 设置为红色
  
  RB_Insert_Fixup(root, z)   # 维持红黑性质
  
  

 
