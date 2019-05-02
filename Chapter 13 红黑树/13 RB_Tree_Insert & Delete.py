# 红黑树的插入与删除


# 定义红黑树结点
class RB_Node:
  def __init__(self, val, color = "RED"):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    self.color = color

# 定义红黑树
class RB_Tree:
  def __init__(self):
    self.root = None


  # 左旋
  def Left_Rotate(self, x):
    y = x.right
    x.right = y.left
    
    if y.left != None:
      y.left.parent = x
        
    y.parent = x.parent
    
    if x.parent == None:
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
     
    y.left = x
    x.parent = y
    
  
  # 右旋
  def Right_Rotate(self, x):
    y = x.left
    x.left = y.right
    
    if y.right != None:
      y.right.parent = x
    
    y.parent = x.parent
    
    if x.parent == None:
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
    
    y.right = x
    x.parent = y
    
   
  # 向红黑树中插入结点
  def RB_Tree_Insert(self, z):
    y = None
    x = self.root

    # 寻找 z 待替换的 None 结点
    while x != None:
      y = x      # 用 y 来存储父结点
      if z.val < x.val:
        x = x.left
      else:
        x = x.right

    z.parent = y   # 设置 z 的父结点

    if y == None:
      self.root = z
    else:
      if z.val < y.val:
        y.left = z
      else:
        y.right = z
   
    z.color = "RED"  # 新插入的结点颜色设置为红色
    
    self.RB_Tree_Insert_Fixup(z)  # 调整整棵树以保持红黑性质
  
  
  # 插入后调整树以维持红黑性质
  def RB_Tree_Insert_Fixup(self，z):   # 只有性质 2 和 4 可能被破坏
    while z.parent and z.parent.color == "RED":  # 性质 4 被破坏，但需要先判断 z 的父结点是否存在
      # 根据 z.parent 和 z.parent.parent 的关系分为两种情形：
      if z.parent == z.parent.parent.left:  # 若第一行条件满足，则 z.parent.parent 必然存在，因为 z.parent 为红色
        y = z.parent.parent.right    # z 的叔结点
        
        if y and y.color == "RED":      # 情况 1：叔结点为红色（此时 z.parent 和 y 都为红色），需先判断 y 是否存在
          z.parent.color = "BLACK"      # 解决方案：将 z.parent 和 y 的颜色置为黑色，z.parent.parent 置为红色，z 结点沿树上升两层。
          y.color = "BLACK"
          z.parent.parent.color = "RED"
          z = z.parent.parent
          
        else:  # 叔结点为黑色
          if z == z.parent.right       # 情况 2：叔结点为黑色 且 z 为 z.parent 的右孩子
            z = z.p                    # 解决方案：z 先上移到 z.parent, 然后通过左旋使 z 下移，
            self.Left_Rotate(z)
          
          z.parent.color = "BLACK"
          z.parent.parent.color = "RED"
          self.Right_Rotate(z.parent.parent)
          
      else:   # z.parent 为 z.parent.parent 的右结点（与上面对称的）
        y = z.parent.parent.left
        
        if y and y.color == "RED":
          z.parent.color = "BLACK"
          y.color = "BLACK"
          z.parent.parent == "RED"
          z = z.parent.parent
          
        else:
          if z == z.parent.right:
            z = z.parent
            self.Left_Rotate(z)
          
          z.parent.color = "BLACK"
          z.parent.parent.color = "RED"
          self.Left_Rotate(z.parent.parent)
      
    root.color = "BLACK"   # 恢复性质 2
      
   
   # 创建一棵红黑树
   def Create_RB_Tree(self, arr):
    
